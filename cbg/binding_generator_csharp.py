from typing import List
import ctypes

from .cpp_binding_generator import BindingGenerator, Define, DefineDependency, CacheMode, ArgCalledBy, Class, Struct, Enum, Code, Property, Function, EnumValue, __get_c_func_name__
from .cpp_binding_generator import __get_c_release_func_name__

# A flow of generating code
# generate
# └─__generate_class__
#   └─__generate_unmanaged_property__
#   └─__generate_unmanaged_func__
#   └─__generate_managed_property__
#     └─__write_managed_func_body__
#   └─__generate_managed_func__
#     └─__write_managed_func_body__
#   └─(destructor)


def get_desc(define: Define, lang: str, elements: []):
    fallback = ''
    if elements[-1].brief is not None:
        fallback = elements[-1].brief.descs[lang]

    return define.get_text(lang, elements, fallback)

class CodeBlock:
    def __init__(self, coder: Code, title: str, after_space: bool = False):
        '''
        a class for generating code block easily
        '''
        self.title = title
        self.coder = coder
        self.after_space = after_space

    def __enter__(self):
        self.coder(self.title)
        self.coder('{')
        self.coder.inc_indent()
        return self

    def __exit__(self, exit_type, exit_value, traceback):
        self.coder.dec_indent()
        self.coder('}')
        if self.after_space:
            self.coder('')

class BindingGeneratorCSharp(BindingGenerator):
    def __init__(self, define: Define, dependencies : List[DefineDependency], lang: str):
        '''
        generator for C#

        Parameters
        ----------
        self_ptr_name : str
            pointer name in the Class

        '''
        super().__init__(define)
        self.namespace = ''
        self.output_path = ''
        self.dll_name = ''
        self.self_ptr_name = 'selfPtr'
        self.lang = lang
        self.dependencies = dependencies

    def get_dependency_namespace(self, obj):
        for dependency in self.dependencies:
            if obj in dependency.define.classes:
                return dependency.namespace

            if obj in dependency.define.structs:
                return dependency.namespace

            if obj in dependency.define.enums:
                return dependency.namespace

        return ''

    def get_alias_or_name(self, type_) -> str:
        namespace = self.get_dependency_namespace(type_)
        if namespace != "":
            namespace += "."

        if type_.alias == None:
            return namespace + type_.name
        else:
            return namespace + type_.alias

    def __generate_enum__(self, enum_: Enum) -> Code:
        code = Code()

        # XML Comment
        brief_comment = get_desc(self.define, self.lang, [enum_])
        if brief_comment != None:
            code('/// <summary>')
            code('/// {}'.format(brief_comment))
            code('/// </summary>')
        # FlagsAttribute
        if enum_.isFlag:
            code('[Flags]')
        code('[Serializable]')

        with CodeBlock(code, 'public enum {} : int'.format(self.get_alias_or_name(enum_))):
            for val in enum_.values:
                # XML Comment
                brief_comment = get_desc(self.define, self.lang, [enum_, val])
                if val.brief != None:
                    code('/// <summary>')
                    code('/// {}'.format(brief_comment))
                    code('/// </summary>')

                # Enum Value Body
                line = val.name
                if val.value != None:
                    line = '{} = {}'.format(line, val.value)
                code(line + ',')
        return code

    def __get_cs_type__(self, type_, is_return=False, called_by: ArgCalledBy = None) -> str:
        ptr = ''
        if called_by == ArgCalledBy.Out:
            ptr = 'out '
        elif called_by == ArgCalledBy.Ref:
            ptr = 'ref '

        if type_ == ctypes.c_byte:
            return ptr + 'byte'

        if type_ == int:
            return ptr + 'int'

        if type_ == float:
            return ptr + 'float'

        if type_ == bool:
            return ptr + 'bool'

        if type_ == ctypes.c_wchar_p:
            return 'string'

        if type_ == ctypes.c_void_p:
            return 'IntPtr'

        if type_ in self.define.classes:
            return self.get_alias_or_name(type_)

        if type_ in self.define.structs:
            if is_return:
                return '{}'.format(type_.alias)
            else:
                return '{}{}'.format(ptr, type_.alias)

        if type_ in self.define.enums:
            return self.get_alias_or_name(type_)

        for dependency in self.dependencies:
            if type_ in dependency.define.classes:
                return self.get_alias_or_name(type_)

            if type_ in dependency.define.structs:
                if is_return:
                    return '{}'.format(type_.alias)
                else:
                    return '{}{}'.format(ptr, type_.alias)

            if type_ in dependency.define.enums:
                return self.get_alias_or_name(type_)

        if type_ is None:
            return 'void'

        assert(False)

    def __get_csc_type__(self, type_, is_return=False, called_by: ArgCalledBy = None) -> str:
        ptr = ''
        if called_by == ArgCalledBy.Out:
            ptr = '[Out] out '
        elif called_by == ArgCalledBy.Ref:
            ptr = '[In, Out] ref '

        if type_ == ctypes.c_byte:
            return ptr + 'byte'

        if type_ == int:
            return ptr + 'int'

        if type_ == float:
            return ptr + 'float'

        if type_ == bool:
            if is_return:
                return 'bool'
            else:
                return '[MarshalAs(UnmanagedType.Bool)] ' + ptr + 'bool'

        if type_ == ctypes.c_wchar_p:
            if is_return:
                return 'IntPtr'
            return '[MarshalAs(UnmanagedType.LPWStr)] string'

        if type_ == ctypes.c_void_p:
            return 'IntPtr'

        defines = [d.define for d in self.dependencies] + [self.define]

        for define in defines:
            if type_ in define.classes:
                return 'IntPtr'

            if type_ in define.structs:
                if is_return:
                    return '{}'.format(type_.alias)
                else:
                    return '{}{}'.format(ptr, type_.alias)

            if type_ in define.enums:
                return 'int'

        if type_ is None:
            return 'void'

        print('Unsupported Type:{}'.format(type_))

        assert(False)

    def __convert_csc_to_cs__(self, type_, name: str, called_by: ArgCalledBy = None) -> str:
        ptr = ''
        if called_by == ArgCalledBy.Out:
            ptr = 'out '
        elif called_by == ArgCalledBy.Ref:
            ptr = 'ref '

        if type_ == ctypes.c_byte or type_ == int or type_ == float or type_ == bool or type_ == ctypes.c_wchar_p or type_ == ctypes.c_void_p:
            return ptr + name

        if type_ in self.define.classes:
            return '{} != null ? {}.{} : IntPtr.Zero'.format(name, name, self.self_ptr_name)

        if type_ in self.define.structs:
            return ptr + name

        if type_ in self.define.enums:
            return '(int){}'.format(name)

        if type_ is None:
            return 'void'

        assert(False)

    def __convert_ret__(self, type_, name: str) -> str:
        if type_ == ctypes.c_byte or type_ == int or type_ == float or type_ == bool or type_ == ctypes.c_void_p:
            return name

        if type_ == ctypes.c_wchar_p:
            return 'System.Runtime.InteropServices.Marshal.PtrToStringUni({})'.format(name)

        defines = [d.define for d in self.dependencies] + [self.define]

        for define in defines:
            if type_ in define.classes:
                class_name = self.get_alias_or_name(type_)
                if type_.cache_mode != CacheMode.NoCache:
                    return '{}.TryGetFromCache({})'.format(class_name, name)
                else:
                    return '{} != null ? new {}(new MemoryHandle({})) : null'.format(name, class_name, name)

            if type_ in define.structs:
                return '{}'.format(name)

            if type_ in define.enums:
                return '({}){}'.format(self.get_alias_or_name(type_), name)

        assert(False)

    def __generate__unmanaged_func__(self, class_: Class, func_: Function) -> Code:
        code = Code()
        fname = __get_c_func_name__(class_, func_)

        args = [self.__get_csc_type__(arg.type_, False, arg.called_by) +
                ' ' + arg.name for arg in func_.args]

        if not func_.is_static and not func_.is_constructor:
            args = ['IntPtr {}'.format(self.self_ptr_name)] + args

        code('[DllImport("{}")]'.format(self.dll_name))
        code('[EditorBrowsable(EditorBrowsableState.Never)]')

        if(func_.return_value.type_ == bool):
            code('[return: MarshalAs(UnmanagedType.U1)]')

        code('private static extern {} {}({});'.format(
            self.__get_csc_type__(func_.return_value.type_, is_return=True), fname, ', '.join(args)))

        return code

    def __generate__unmanaged_property_(self, class_: Class, prop_: Property) -> Code:
        code = Code()
        result = ''
        if prop_.has_getter:
            result += str(self.__generate__unmanaged_func__(class_,
                                                            prop_.getter_as_func()))
        if prop_.has_setter:
            result += str(self.__generate__unmanaged_func__(class_,
                                                            prop_.setter_as_func()))
        code(result)
        return code

    def __write_managed_function_body__(self, code: Code, class_: Class, func_: Function, callByDerived_ = False):
        fname = __get_c_func_name__(class_, func_)
        # call a function
        args = [self.__convert_csc_to_cs__(
            arg.type_, arg.name, arg.called_by) for arg in func_.args]

        if not func_.is_static and not func_.is_constructor:
            args = [self.self_ptr_name] + args

        for a in func_.args:
            if not a.nullable and (a.type_ in self.define.classes or a.type_ == ctypes.c_wchar_p):
                code('if ({} == null) throw new ArgumentNullException(nameof({}), "引数がnullです");'.format(
                    a.name, a.name))

        if func_.is_constructor:
            if callByDerived_:
                code('// Dummy function.')
            else:
                code('{} = {}({});'.format(self.self_ptr_name, fname, ', '.join(args)))
        else:
            if func_.return_value.type_ is None:
                code('{}({});'.format(fname, ', '.join(args)))
            else:
                code('var ret = {}({});'.format(fname, ', '.join(args)))
                code('return {};'.format(
                    self.__convert_ret__(func_.return_value.type_, 'ret')))

    def __generate__managed_func__(self, class_: Class, func_: Function) -> Code:
        code = Code()
        fname = __get_c_func_name__(class_, func_)

        args = [self.__get_cs_type__(
            arg.type_, False, arg.called_by) + ' ' + arg.name for arg in func_.args]

        # XML comment
        brief_comment = get_desc(self.define, self.lang, [class_, func_])
        if brief_comment != "":
            code('/// <summary>')
            code('/// {}'.format(brief_comment))
            code('/// </summary>')
            for arg in func_.args:
                brief_comment = get_desc(self.define, self.lang, [class_, func_, arg])
                if brief_comment != "":
                    code('/// <param name="{}">{}</param>'.format(arg.name,brief_comment))

            argcount = 0
            exc_message = '/// <exception cref="ArgumentNullException">'
            for a in func_.args:
                if not a.nullable and (a.type_ in self.define.classes or a.type_ == ctypes.c_wchar_p):
                    if argcount > 0:
                        exc_message += ', '
                    exc_message += '<paramref name="{}"/>'.format(a.name)
                    argcount += 1
            if argcount == 1:
                code(exc_message + 'がnull</exception>')
            else:
                if argcount > 1:
                    code(exc_message + 'のいずれかがnull</exception>')

            brief_comment = get_desc(self.define, self.lang, [class_, func_, func_.return_value])
            if brief_comment != "":
                code(
                    '/// <returns>{}</returns>'.format(brief_comment))

        # cache repo
        if func_.return_value.cache_mode() == CacheMode.Cache:
            return_type_name = self.__get_cs_type__(
                func_.return_value.type_, is_return=True)
            cache_code = 'private Dictionary<IntPtr, WeakReference<{}>> cache{} = new Dictionary<IntPtr, WeakReference<{}>>();'
            code('[EditorBrowsable(EditorBrowsableState.Never)]')
            code(cache_code.format(return_type_name, func_.name, return_type_name))
        elif func_.return_value.cache_mode() == CacheMode.ThreadSafeCache:
            return_type_name = self.__get_cs_type__(
                func_.return_value.type_, is_return=True)
            cache_code = 'private ConcurrentDictionary<IntPtr, WeakReference<{}>> cache{} = new ConcurrentDictionary<IntPtr, WeakReference<{}>>();'
            code('[EditorBrowsable(EditorBrowsableState.Never)]')
            code(cache_code.format(return_type_name, func_.name, return_type_name))

        # determine signature
        determines = []

        if func_.is_public:
            determines += ['public']
        else:
            determines += ['internal']

        if func_.is_static:
            determines += ['static']

        if func_.is_constructor:
            func_title = '{} {}({})'.format(' '.join(determines), self.get_alias_or_name(class_), ', '.join(args))
            if class_.base_class != None:
                func_title += ' : base({})'.format(', '.join(['true'] + [arg.name for arg in func_.args]))
            with CodeBlock(code, func_title):
                self.__write_managed_function_body__(code, class_, func_)
            code('')
            func_title = 'protected {}({})'.format(self.get_alias_or_name(class_), ', '.join(['bool calledByDerived'] + args))
            if class_.base_class != None:
                func_title += ' : base({})'.format(', '.join(['calledByDerived'] + [arg.name for arg in func_.args]))
            with CodeBlock(code, func_title):
                self.__write_managed_function_body__(code, class_, func_, True)
        else:
            func_title = '{} {} {}({})'.format(' '.join(determines), self.__get_cs_type__(func_.return_value.type_, is_return=True), func_.name, ', '.join(args))
            with CodeBlock(code, func_title):
                self.__write_managed_function_body__(code, class_, func_)

        return code

    def __write_getter_(self, code: Code, class_: Class, prop_: Property):
        with CodeBlock(code, 'get'):
            if prop_.has_setter:
                with CodeBlock(code, 'if (_{} != null)'.format(prop_.name)):
                    if isinstance(prop_.type_, Class) or (prop_.type_ == ctypes.c_wchar_p):
                        code('return _{};'.format(prop_.name))
                    else:
                        code('return _{}.Value;'.format(prop_.name))
            self.__write_managed_function_body__(
                code, class_, prop_.getter_as_func())

    def __write_setter_(self, code: Code, class_: Class, prop_: Property):
        with CodeBlock(code, 'set'):
            if prop_.has_getter:
                if not prop_.nullable and (prop_.type_ in self.define.classes or prop_.type_ == ctypes.c_wchar_p):
                    code('_{} = value ?? throw new ArgumentNullException(nameof(value), "設定しようとした値がnullです");'.format(
                        prop_.name))
                else:
                    code('_{} = value;'.format(prop_.name))
            self.__write_managed_function_body__(
                code, class_, prop_.setter_as_func())

    def __generate__managed_property_(self, class_: Class, prop_: Property) -> Code:
        code = Code()

        # cannot generate property with no getter and no setter
        if not prop_.has_getter and not prop_.has_setter:
            return code

        # XML comment
        brief_comment = get_desc(self.define, self.lang, [class_, prop_])
        if brief_comment != '':
            code('/// <summary>')
            code('/// {}'.format(brief_comment))
            code('/// </summary>')

            if not prop_.nullable and (prop_.type_ in self.define.classes or prop_.type_ == ctypes.c_wchar_p):
                code(
                    '/// <exception cref="ArgumentNullException">設定しようとした値がnull</exception>')

        type_name = self.__get_cs_type__(prop_.type_, is_return=True)
        access = ''
        if prop_.is_public:
            access = 'public'
        else:
            access = 'internal'
        with CodeBlock(code, '{} {} {}'.format(access, type_name, prop_.name)):
            if prop_.has_getter:
                self.__write_getter_(code, class_, prop_)
            if prop_.has_setter:
                self.__write_setter_(code, class_, prop_)

        if prop_.has_setter and prop_.has_getter:
            back_type = type_name
            if not (isinstance(prop_.type_, Class) or (prop_.type_ == ctypes.c_wchar_p)):
                back_type += '?'
            code('private {} _{};'.format(back_type, prop_.name))

        return code

    def __write_cache_getter__(self, code: Code, class_: Class):
        release_func_name = __get_c_func_name__(class_, Function('Release'))

        new_ = ''
        if class_.base_class != None:
            new_ = 'new'
        body = '''[EditorBrowsable(EditorBrowsableState.Never)]
public static {2} {0} TryGetFromCache(IntPtr native)
{{
    if(native == IntPtr.Zero) return null;

    if(cacheRepo.ContainsKey(native))
    {{
        {0} cacheRet;
        cacheRepo[native].TryGetTarget(out cacheRet);
        if(cacheRet != null)
        {{
            {1}(native);
            return cacheRet;
        }}
        else
        {{
            cacheRepo.Remove(native);
        }}
    }}

    var newObject = new {0}(new MemoryHandle(native));
    cacheRepo[native] = new WeakReference<{0}>(newObject);
    return newObject;
}}
'''.format(self.get_alias_or_name(class_), release_func_name, new_)
        lines = body.split('\n')
        for line in lines:
            code(line)

    def __write_threadsafe_cache_getter__(self, code: Code, class_: Class):
        release_func_name = __get_c_func_name__(class_, Function('Release'))

        new_ = ''
        if class_.base_class != None:
            new_ = 'new'

        body = '''[EditorBrowsable(EditorBrowsableState.Never)]
        internal static {2} {0} TryGetFromCache(IntPtr native)
{{
    if(native == IntPtr.Zero) return null;

    if(cacheRepo.ContainsKey(native))
    {{
        {0} cacheRet;
        cacheRepo[native].TryGetTarget(out cacheRet);
        if(cacheRet != null)
        {{
            {1}(native);
            return cacheRet;
        }}
        else
        {{
            cacheRepo.TryRemove(native, out _);
        }}
    }}

    var newObject = new {0}(new MemoryHandle(native));
    cacheRepo.TryAdd(native, new WeakReference<{0}>(newObject));
    return newObject;
}}
'''.format(self.get_alias_or_name(class_), release_func_name, new_)
        lines = body.split('\n')
        for line in lines:
            code(line)

    def __generate_class__(self, class_: Class) -> Code:
        code = Code()

        class_name = self.get_alias_or_name(class_)

        # XML comment
        brief_comment = get_desc(self.define, self.lang, [class_])
        if brief_comment != None:
            code('/// <summary>')
            code('/// {}'.format(brief_comment))
            code('/// </summary>')

        # SerializableAttribute
        if class_.SerializeType > 0:
            code('[Serializable]')

        # inheritance
        inheritance = ""
        inheritCount = 0
        if class_.base_class != None:
            inheritCount += 1
            inheritance = ' : {}'.format(self.get_alias_or_name(class_.base_class))

        # ISerializable
        if (class_.SerializeType >= 2):
            if (inheritCount == 0):
                inheritance += ' : '
            else:
                inheritance += ', '
            inheritance += 'ISerializable'
            inheritCount += 1

            if class_.handleCache:
                inheritance += ', ICacheKeeper<{}>'.format(class_name)
                inheritCount += 1

        # IDeserializationCallBack
        if (class_.CallBackType > 0):
            if (inheritCount == 0):
                inheritance += ' : '
            else:
                inheritance += ', '
            inheritance += 'IDeserializationCallback'
            inheritCount += 1

        # class body

        access = 'internal'
        if class_.is_public:
            access = 'public'

        sealed = ''
        if (class_.is_Sealed):
            sealed = 'sealed '

        with CodeBlock(code, '{} {}partial class {}{}'.format(access, sealed, class_name, inheritance)):
            code('#region unmanaged')
            code('')

            # cache repo
            if class_.cache_mode == CacheMode.Cache:
                cache_code = 'private static Dictionary<IntPtr, WeakReference<{}>> cacheRepo = new Dictionary<IntPtr, WeakReference<{}>>();'
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code(cache_code.format(class_name, class_name))
                code('')
                self.__write_cache_getter__(code, class_)
            elif class_.cache_mode == CacheMode.ThreadSafeCache:
                cache_code = 'private static ConcurrentDictionary<IntPtr, WeakReference<{}>> cacheRepo = new ConcurrentDictionary<IntPtr, WeakReference<{}>>();'
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code(cache_code.format(class_name, class_name))
                code('')
                self.__write_threadsafe_cache_getter__(code, class_)

            # unmanaged pointer
            if class_.base_class == None:
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code('internal IntPtr {} = IntPtr.Zero;'.format(self.self_ptr_name))

            # extern unmanaged functions
            for func_ in [f for f in class_.funcs if len(f.targets) == 0 or 'csharp' in f.targets]:
                code(self.__generate__unmanaged_func__(class_, func_))
            for prop_ in class_.properties:
                code(self.__generate__unmanaged_property_(class_, prop_))

            # releasing function
            release_func = Function('Release')
            code(self.__generate__unmanaged_func__(class_, release_func))
            code('#endregion')
            code('')

            # constructor
            if class_.base_class == None:
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, 'internal {}(MemoryHandle handle)'.format(class_name), True):
                    code('{} = handle.selfPtr;'.format(self.self_ptr_name))
            else:
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, 'internal {}(MemoryHandle handle) : base(handle)'.format(class_name), True):
                    code('{} = handle.selfPtr;'.format(self.self_ptr_name))

            # properties
            for prop_ in class_.properties:
                if not prop_.onlyExtern:
                    code(self.__generate__managed_property_(class_, prop_))

            # managed functions
            for func_ in [f for f in class_.funcs if not f.onlyExtern and (len(f.targets) == 0 or 'csharp' in f.targets)]:
                code(self.__generate__managed_func__(class_, func_))

            # ISerializable
            if class_.SerializeType >= 2:
                code('')
                code('#region ISerialiable')

                # names
                code('')
                code('#region SerializeName')
                for p in class_.properties:
                    if p.serialized:
                        code('[EditorBrowsable(EditorBrowsableState.Never)]')
                        code('private const string S_{} = "S_{}";'.format(
                            p.name, p.name))
                code('#endregion')
                code('')

                if class_.CallBackType > 0:
                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    code('private SerializationInfo seInfo;')
                    code('')

                title_GetObj = ''
                title_Const = '{}(SerializationInfo info, StreamingContext context)'.format(
                    class_name)

                if class_.is_Sealed:
                    title_Const = 'private ' + title_Const
                else:
                    title_Const = 'protected ' + title_Const

                if class_.base_class != None and class_.base_class.SerializeType >= 2:
                    title_Const += ' : base(info, context)'
                    title_GetObj = 'protected override void '
                else:
                    if class_.is_Sealed:
                        title_GetObj = 'void ISerializable.'
                    else:
                        title_GetObj = 'protected virtual void '
                    if class_.constructor_count == 1:
                        title_Const += ' : this()'
                    else:
                        if class_.base_class == None:
                            title_Const += ' : this(new MemoryHandle(IntPtr.Zero))'

                title_GetObj += 'GetObjectData(SerializationInfo info, StreamingContext context)'

                # Deserialize Constructor
                code('/// <summary>')
                code(
                    '/// シリアライズされたデータをもとに<see cref="{}"/>のインスタンスを生成します。'.format(class_name))
                code('/// </summary>')
                code('/// <param name="info">シリアライズされたデータを格納するオブジェクト</param>')
                code('/// <param name="context">送信元の情報</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, title_Const, True):
                    if class_.CallBackType > 0:
                        code('seInfo = info;')
                    else:
                        self.__deserialize__(class_, code, 'info')

                    code('')
                    code('OnDeserialize_Constructor(info, context);')

                # GetObjectData
                code('/// <summary>')
                code('/// シリアライズするデータを設定します。')
                code('/// </summary>')
                code('/// <param name="info">シリアライズされるデータを格納するオブジェクト</param>')
                code('/// <param name="context">送信先の情報</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, title_GetObj):
                    if class_.SerializeType == 3 and class_.base_class != None and class_.base_class.SerializeType >= 2:
                        code('base.GetObjectData(info, context);')
                    else:
                        code(
                            'if (info == null) throw new ArgumentNullException(nameof(info), "引数がnullです");')

                    code('')

                    for p in class_.properties:
                        if p.serialized:
                            code('info.AddValue(S_{}, {});'.format(p.name, p.name))

                    code('')

                    code('OnGetObjectData(info, context);')
                if (class_.base_class == None or class_.base_class.SerializeType < 2) and not class_.is_Sealed:
                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    code(
                        'void ISerializable.GetObjectData(SerializationInfo info, StreamingContext context) => GetObjectData(info, context);')

                # OnGetObjectData
                code('')
                code('/// <summary>')
                if class_.is_Sealed and (class_.base_class == None or class_.base_class.SerializeType < 2):
                    code(
                        '/// <see cref="ISerializable.GetObjectData(SerializationInfo, StreamingContext)"/>内で実行されます。')
                else:
                    code(
                        '/// <see cref="GetObjectData(SerializationInfo, StreamingContext)"/>内で実行されます。')
                code('/// </summary>')
                code('/// <param name="info">シリアライズされるデータを格納するオブジェクト</param>')
                code('/// <param name="context">送信先の情報</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code(
                    'partial void OnGetObjectData(SerializationInfo info, StreamingContext context);')

                # OnDeserialization_Constructor
                code('')
                code('/// <summary>')
                code(
                    '/// <see cref="{}(SerializationInfo, StreamingContext)"/>内で実行します。'.format(class_name))
                code('/// </summary>')
                code('/// <param name="info">シリアライズされたデータを格納するオブジェクト</param>')
                code('/// <param name="context">送信元の情報</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code(
                    'partial void OnDeserialize_Constructor(SerializationInfo info, StreamingContext context);')

                # Deserialize_GetPtr
                code('')
                code('/// <summary>')
                if class_.CallBackType > 0:
                    code(
                        '/// <see cref="IDeserializationCallback.OnDeserialization"/>内で呼び出されます。')
                else:
                    code(
                        '/// <see cref="{}(SerializationInfo, StreamingContext)"/>内で呼び出される'.format(class_name))
                code('/// デシリアライズ時にselfPtrを取得する操作をここに必ず書くこと')
                code('/// </summary>')
                code('/// <param name="ptr">selfPtrとなる値 初期値である<see cref="IntPtr.Zero"/>のままだと<see cref="SerializationException"/>がスローされる</param>')
                code('/// <param name="info">シリアライズされたデータを格納するオブジェクト</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code(
                    'partial void Deserialize_GetPtr(ref IntPtr ptr, SerializationInfo info);')

                title_get = ''
                if class_.base_class != None and class_.base_class.SerializeType >= 2 and class_.base_class.handleCache:
                    title_get = 'protected private override '
                else:
                    if class_.is_Sealed:
                        title_get = 'private '
                    else:
                        title_get = 'protected private virtual '
                title_get += 'IntPtr Call_GetPtr(SerializationInfo info)'

                code('')
                code('/// <summary>')
                code('/// 呼び出し禁止')
                code('/// </summary>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, title_get, True):
                    code('var ptr = IntPtr.Zero;')
                    code('Deserialize_GetPtr(ref ptr, info);')
                    code('return ptr;')

                # Unsetter_Deserialize
                title_des = ''
                if (class_.is_Sealed):
                    title_des = 'private'
                else:
                    title_des = 'protected private'
                title_des += ' void {}_Unsetter_Deserialize(SerializationInfo info'.format(
                    class_name)

                title_des_args = ''
                for p in class_.properties:
                    if p.serialized and not p.has_setter:
                        title_des_args += ', out {} {}'.format(
                            self.__get_cs_type__(p.type_), p.name)

                title_des_args += ')'
                if title_des_args != ')':
                    code('/// <summary>')
                    if class_.CallBackType > 0:
                        code(
                            '/// <see cref="IDeserializationCallback.OnDeserialization"/>でデシリアライズされなかったオブジェクトを呼び出します。')
                    else:
                        code(
                            '/// <see cref="{}(SerializationInfo, StreamingContext)"/>でデシリアライズされなかったオブジェクトを呼び出します。'.format(class_name))
                    code('/// </summary>')
                    code('/// <param name="info">シリアライズされたデータを格納するオブジェクト</param>')
                    for p in class_.properties:
                        if p.serialized and not p.has_setter:
                            code(
                                '/// <param name="{}"><see cref="{}.{}"/></param>'.format(p.name, class_name, p.name))
                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    with CodeBlock(code, title_des + title_des_args, True):
                        self.__deserialize_nosetter__(class_, code)

                # ICacheKeeper
                if class_.handleCache:
                    code('#region ICacheKeeper')
                    code('')

                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    code('IDictionary<IntPtr, WeakReference<{}>> ICacheKeeper<{}>.CacheRepo => cacheRepo;'.format(
                        class_name, class_name))
                    code('')

                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    with CodeBlock(code, 'IntPtr ICacheKeeper<{}>.Self'.format(class_name), True):
                        code('get => selfPtr;')
                        with CodeBlock(code, 'set', False):
                            code('selfPtr = value;')

                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    code('void ICacheKeeper<{}>.Release(IntPtr native) => cbg_{}_Release(native);'.format(
                        class_name, class_name))

                    code('')

                    code('#endregion')

                code('')
                code('#endregion')
                code('')

            # OnDeserializationCallback
            if class_.CallBackType > 0:
                title = ''
                if class_.base_class != None and class_.base_class.CallBackType > 0:
                    title = 'protected override void '
                else:
                    if class_.is_Sealed:
                        title = 'void IDeserializationCallback.'
                    else:
                        title = 'protected virtual void '
                title += 'OnDeserialization(object sender)'

                code('/// <summary>')
                code('/// デシリアライズ時に実行')
                code('/// </summary>')
                code('/// <param name="sender">現在はサポートされていない 常にnullを返します。</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                with CodeBlock(code, title):
                    if class_.SerializeType >= 2:
                        code('if (seInfo == null) return;')
                        code('')
                        self.__deserialize__(class_, code, 'seInfo')

                        if (class_.base_class != None and class_.base_class.CallBackType > 0):
                            code('base.OnDeserialization(sender);')
                        code('')

                    code('OnDeserialize_Method(sender);')

                    if class_.SerializeType >= 2:
                        code('')
                        code('seInfo = null;')

                if class_.base_class == None and not class_.is_Sealed:
                    code('[EditorBrowsable(EditorBrowsableState.Never)]')
                    code(
                        'void IDeserializationCallback.OnDeserialization(object sender) => OnDeserialization(sender);')

                # OnDeserialize_Method
                code('/// <summary>')
                if (class_.base_class == None or class_.base_class.CallBackType == 0) and class_.is_Sealed:
                    code(
                        '/// <see cref="IDeserializationCallback.OnDeserialization"/>中で実行されます。')
                else:
                    code(
                        '/// <see cref="IDeserializationCallback.OnDeserialization"/>中で実行されます。')
                code('/// </summary>')
                code('/// <param name="sender">現在はサポートされていない 常にnullを返す</param>')
                code('[EditorBrowsable(EditorBrowsableState.Never)]')
                code('partial void OnDeserialize_Method(object sender);')
                code('')

            # destructor
            code('/// <summary>')
            code('/// <see cref="{}"/>のインスタンスを削除します。'.format(class_name))
            code('/// </summary>')
            with CodeBlock(code, '~{}()'.format(class_name)):
                with CodeBlock(code, 'lock (this) '):
                    with CodeBlock(code, 'if ({} != IntPtr.Zero)'.format(self.self_ptr_name)):
                        code('{}({});'.format(__get_c_release_func_name__(
                            class_), self.self_ptr_name))
                        code('{} = IntPtr.Zero;'.format(self.self_ptr_name))

        return code

    def __deserialize__(self, class_: Class, code: Code, info: str) -> str:
        if class_.handleCache:
            if class_.base_class != None and class_.base_class.handleCache:
                code('var ptr = selfPtr;')
                code('if (ptr == IntPtr.Zero) ptr = Call_GetPtr({});'.format(info))
            else:
                code('var ptr = Call_GetPtr({});'.format(info))
            code('')
            code(
                'if (ptr == IntPtr.Zero) throw new SerializationException("インスタンス生成に失敗しました");')
            if class_.cache_mode == CacheMode.ThreadSafeCache:
                code('CacheHelper.CacheHandlingOnDeserializationConcurrent(this, ptr);')
            else:
                code('CacheHelper.CacheHandlingOnDeserialization(this, ptr);')
            code('')
        else:
            code('selfPtr = Call_GetPtr({});'.format(info))
            code(
                'if (selfPtr == IntPtr.Zero) throw new SerializationException("インスタンス生成に失敗しました");')
            code('')
        for p in class_.properties:
            if p.serialized and p.has_setter:
                c = '{} = {}.{}'.format(
                    p.name, info, self.__write_getvalue__(p))
                if p.type_ in self.define.classes and p.type_.CallBackType > 0:
                    code('var ' + c)
                    code(
                        '((IDeserializationCallback){})?.OnDeserialization(null);'.format(p.name))
                    code('this.{} = {};'.format(p.name, p.name))
                else:
                    code(c)

    def __deserialize_nosetter__(self, class_: Class, code: Code) -> str:
        for p in class_.properties:
            if p.serialized and not p.has_setter:
                code('{} = info.{}'.format(p.name, self.__write_getvalue__(p)))
                if p.type_ in self.define.classes and p.type_.CallBackType > 0:
                    code(
                        '((IDeserializationCallback){}).OnDeserialization(null);'.format(p.name))

    def __write_getvalue__(self, p: Property) -> str:
        if p.type_ == ctypes.c_byte:
            return 'GetByte(S_{});'.format(p.name)
        if p.type_ == int:
            return 'GetInt32(S_{});'.format(p.name)
        if p.type_ == bool:
            return 'GetBoolean(S_{});'.format(p.name)
        if p.type_ == float:
            return 'GetSingle(S_{});'.format(p.name)
        if p.type_ == ctypes.c_wchar_p:
            if p.null_deserialized:
                return 'GetString(S_{});'.format(p.name)
            else:
                return 'GetString(S_{}) ?? throw new SerializationException("デシリアライズに失敗しました");'.format(p.name)
        if p.type_ in self.define.structs:
            return 'GetValue<{}>(S_{});'.format(p.type_.alias, p.name)
        if p.type_ in self.define.classes and not p.null_deserialized:
            return 'GetValue<{}>(S_{}) ?? throw new SerializationException("デシリアライズに失敗しました");'.format(self.get_alias_or_name(p.type_), p.name)
        if p.type_ in self.define.enums:
            return 'GetValue<{}>(S_{});'.format(self.get_alias_or_name(p.type_), p.name)
        return 'GetValue<{}>(S_{});'.format(p.type_.name, p.name)

    def generate(self):
        code = Code()

        # add Waring
        code('// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        code('// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        code('//')
        code('//   このファイルは自動生成されました。')
        code('//   このファイルへの変更は消失することがあります。')
        code('//')
        code('//   THIS FILE IS AUTO GENERATED.')
        code('//   YOUR COMMITMENT ON THIS FILE WILL BE WIPED. ')
        code('//')
        code('// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        code('// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        # declare using
        code('using System;')
        code('using System.ComponentModel;')
        code('using System.Collections.Generic;')
        code('using System.Collections.Concurrent;')
        code('using System.Runtime.InteropServices;')
        code('using System.Runtime.Serialization;')
        code('')

        # declare namespace
        if self.namespace != '':
            code('namespace {}'.format(self.namespace))
            code('{')
            code.inc_indent()

        # a struct for memory management
        code('[EditorBrowsable(EditorBrowsableState.Never)]')
        with CodeBlock(code, 'struct MemoryHandle', True):
            code('public IntPtr selfPtr;')  # internal?
            with CodeBlock(code, 'public MemoryHandle(IntPtr p)'):  # internal?
                code('this.selfPtr = p;')

        # enum group
        for enum_ in self.define.enums:
            code(self.__generate_enum__(enum_))

        # class group
        for class_ in self.define.classes:
            code(self.__generate_class__(class_))

        # close namespace
        if self.namespace != '':
            code.dec_indent()
            code('}')

        if self.output_path == '':
            print('please specify an output path')
        else:
            with open(self.output_path, mode='w', encoding='utf-8', newline="\r\n") as f:
                f.write(str(code))
