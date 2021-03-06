// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//
//   このファイルは自動生成されました。
//   このファイルへの変更は消失することがあります。
//
//   THIS FILE IS AUTO GENERATED.
//   YOUR COMMITMENT ON THIS FILE WILL BE WIPED. 
//
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#include "AutoGeneratedCoreBindings.h"

namespace HelloWorldA
{
    static std::shared_ptr<DynamicLinkLibrary> dll = nullptr;
    std::shared_ptr<DynamicLinkLibrary>& GetLibrary()
    {
        if(dll != nullptr) return dll;
        dll = std::shared_ptr<DynamicLinkLibrary>(new DynamicLinkLibrary());
        if(!dll->Load(ConvertSharedObjectPath("CoreLib").c_str())) dll = nullptr;
        return dll;
    }
    
    std::mutex ClassAlias_Cpp::mtx;
    
    std::unordered_map<void*, std::weak_ptr<ClassAlias_Cpp> > ClassAlias_Cpp::cacheRepo;
    
    void* ClassAlias_Cpp::cbg_ClassAlias_Cpp_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassAlias_Cpp_Constructor_0");
        return proc();
    }
    
    void* ClassAlias_Cpp::cbg_ClassAlias_Cpp_FuncSimple(void* selfPtr)
    {
        typedef void* (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassAlias_Cpp_FuncSimple");
        return proc(selfPtr);
    }
    
    void ClassAlias_Cpp::cbg_ClassAlias_Cpp_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassAlias_Cpp_AddRef");
        proc(selfPtr);
    }
    
    void ClassAlias_Cpp::cbg_ClassAlias_Cpp_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassAlias_Cpp_Release");
        proc(selfPtr);
    }
    
    ClassAlias_Cpp::ClassAlias_Cpp(void* handle)
    {
        selfPtr = handle;
    }
    
    ClassAlias_Cpp::ClassAlias_Cpp(bool calledByDerived)
    {
        // Dummy function.
    }
    
    ClassAlias_Cpp::ClassAlias_Cpp()
    {
        selfPtr = cbg_ClassAlias_Cpp_Constructor_0();
    }
    
    std::shared_ptr<ClassAlias_Cpp> ClassAlias_Cpp::FuncSimple()
    {
        auto ret = cbg_ClassAlias_Cpp_FuncSimple(selfPtr);
        return std::shared_ptr<ClassAlias_Cpp>(ret != nullptr ? new ClassAlias_Cpp(ret) : nullptr);
    }
    
    ClassAlias_Cpp::~ClassAlias_Cpp()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_ClassAlias_Cpp_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
    std::mutex ClassA::mtx;
    
    std::unordered_map<void*, std::weak_ptr<ClassA> > ClassA::cacheRepo;
    
    void* ClassA::cbg_ClassA_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_Constructor_0");
        return proc();
    }
    
    void ClassA::cbg_ClassA_FuncSimple(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncSimple");
        proc(selfPtr);
    }
    
    void ClassA::cbg_ClassA_FuncArgInt(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncArgInt");
        proc(selfPtr, value);
    }
    
    void ClassA::cbg_ClassA_FuncArgFloatBoolStr(void* selfPtr, float value1, int value2, const char16_t* value3)
    {
        typedef void (*proc_t)(void* selfPtr, float value1, int value2, const char16_t* value3);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncArgFloatBoolStr");
        proc(selfPtr, value1, value2, value3);
    }
    
    void ClassA::cbg_ClassA_FuncArgStruct(void* selfPtr, void* value1)
    {
        typedef void (*proc_t)(void* selfPtr, void* value1);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncArgStruct");
        proc(selfPtr, value1);
    }
    
    void ClassA::cbg_ClassA_FuncArgClass(void* selfPtr, void* value1)
    {
        typedef void (*proc_t)(void* selfPtr, void* value1);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncArgClass");
        proc(selfPtr, value1);
    }
    
    int ClassA::cbg_ClassA_FuncReturnInt(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnInt");
        return proc(selfPtr);
    }
    
    int ClassA::cbg_ClassA_FuncReturnBool(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnBool");
        return proc(selfPtr);
    }
    
    float ClassA::cbg_ClassA_FuncReturnFloat(void* selfPtr)
    {
        typedef float (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnFloat");
        return proc(selfPtr);
    }
    
    StructA_C ClassA::cbg_ClassA_FuncReturnStruct(void* selfPtr)
    {
        typedef StructA_C (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnStruct");
        return proc(selfPtr);
    }
    
    void* ClassA::cbg_ClassA_FuncReturnClass(void* selfPtr)
    {
        typedef void* (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnClass");
        return proc(selfPtr);
    }
    
    const char16_t* ClassA::cbg_ClassA_FuncReturnString(void* selfPtr)
    {
        typedef const char16_t* (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnString");
        return proc(selfPtr);
    }
    
    int ClassA::cbg_ClassA_FuncReturnStatic()
    {
        typedef int (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_FuncReturnStatic");
        return proc();
    }
    
    void* ClassA::cbg_ClassA_GetBReference(void* selfPtr)
    {
        typedef void* (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_GetBReference");
        return proc(selfPtr);
    }
    
    int ClassA::cbg_ClassA_GetEnumA(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_GetEnumA");
        return proc(selfPtr);
    }
    
    void ClassA::cbg_ClassA_SetEnumA(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_SetEnumA");
        proc(selfPtr, value);
    }
    
    void ClassA::cbg_ClassA_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_AddRef");
        proc(selfPtr);
    }
    
    void ClassA::cbg_ClassA_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassA_Release");
        proc(selfPtr);
    }
    
    ClassA::ClassA(void* handle)
    {
        selfPtr = handle;
    }
    
    std::shared_ptr<ClassB> ClassA::get_BReference()
    {
        auto ret = cbg_ClassA_GetBReference(selfPtr);
        return ClassB::TryGetFromCache(ret);
    }
    
    Animal ClassA::get_EnumA()
    {
        return _EnumA;
        auto ret = cbg_ClassA_GetEnumA(selfPtr);
        return (Animal)ret;
    }
    void ClassA::set_EnumA(Animal value)
    {
        _EnumA = value;
        cbg_ClassA_SetEnumA(selfPtr, (int)value);
    }
    
    ClassA::ClassA(bool calledByDerived)
    {
        // Dummy function.
    }
    
    ClassA::ClassA()
    {
        selfPtr = cbg_ClassA_Constructor_0();
    }
    
    void ClassA::FuncSimple()
    {
        cbg_ClassA_FuncSimple(selfPtr);
    }
    
    void ClassA::FuncArgInt(int value)
    {
        cbg_ClassA_FuncArgInt(selfPtr, value);
    }
    
    void ClassA::FuncArgFloatBoolStr(float value1, bool value2, std::basic_string<char16_t> value3)
    {
        cbg_ClassA_FuncArgFloatBoolStr(selfPtr, value1, value2, value3.c_str());
    }
    
    /**
     @brief Processes a structA.
     */
    void ClassA::FuncArgStruct(std::shared_ptr<StructA_C> value1)
    {
        cbg_ClassA_FuncArgStruct(selfPtr, value1.get());
    }
    
    void ClassA::FuncArgClass(std::shared_ptr<ClassB> value1)
    {
        cbg_ClassA_FuncArgClass(selfPtr, value1 != nullptr ? (value1->selfPtr) : nullptr);
    }
    
    /**
     @brief Returns some integer.
     */
    int ClassA::FuncReturnInt()
    {
        auto ret = cbg_ClassA_FuncReturnInt(selfPtr);
        return ret;
    }
    
    bool ClassA::FuncReturnBool()
    {
        auto ret = cbg_ClassA_FuncReturnBool(selfPtr);
        return ret;
    }
    
    float ClassA::FuncReturnFloat()
    {
        auto ret = cbg_ClassA_FuncReturnFloat(selfPtr);
        return ret;
    }
    
    StructA_C ClassA::FuncReturnStruct()
    {
        auto ret = cbg_ClassA_FuncReturnStruct(selfPtr);
        return ret;
    }
    
    std::shared_ptr<ClassB> ClassA::FuncReturnClass()
    {
        auto ret = cbg_ClassA_FuncReturnClass(selfPtr);
        return ClassB::TryGetFromCache(ret);
    }
    
    std::basic_string<char16_t> ClassA::FuncReturnString()
    {
        auto ret = cbg_ClassA_FuncReturnString(selfPtr);
        return ret;
    }
    
    int ClassA::FuncReturnStatic()
    {
        auto ret = cbg_ClassA_FuncReturnStatic();
        return ret;
    }
    
    ClassA::~ClassA()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_ClassA_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
    std::mutex ClassB::mtx;
    
    std::unordered_map<void*, std::weak_ptr<ClassB> > ClassB::cacheRepo;
    std::shared_ptr<ClassB> ClassB::TryGetFromCache(void* native)
    {
        if(native == nullptr) return nullptr;
        
        if(cacheRepo.count(native))
        {
            std::shared_ptr<ClassB> cacheRet = cacheRepo[native].lock();
            if(cacheRet.get() != nullptr)
            {
                cbg_ClassB_Release(native);
                return cacheRet;
            }
            else
            {
                cacheRepo.erase(native);
            }
        }
        
        std::shared_ptr<ClassB> newObject(new ClassB(native));
        cacheRepo[native] = newObject;
        return newObject;
    }
    
    
    void* ClassB::cbg_ClassB_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_Constructor_0");
        return proc();
    }
    
    void ClassB::cbg_ClassB_SetValue(void* selfPtr, float value)
    {
        typedef void (*proc_t)(void* selfPtr, float value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_SetValue");
        proc(selfPtr, value);
    }
    
    void ClassB::cbg_ClassB_SetEnum(void* selfPtr, int enumValue)
    {
        typedef void (*proc_t)(void* selfPtr, int enumValue);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_SetEnum");
        proc(selfPtr, enumValue);
    }
    
    int ClassB::cbg_ClassB_GetEnum(void* selfPtr, int id)
    {
        typedef int (*proc_t)(void* selfPtr, int id);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_GetEnum");
        return proc(selfPtr, id);
    }
    
    int ClassB::cbg_ClassB_GetMyProperty(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_GetMyProperty");
        return proc(selfPtr);
    }
    
    void ClassB::cbg_ClassB_SetMyProperty(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_SetMyProperty");
        proc(selfPtr, value);
    }
    
    void ClassB::cbg_ClassB_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_AddRef");
        proc(selfPtr);
    }
    
    void ClassB::cbg_ClassB_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassB_Release");
        proc(selfPtr);
    }
    
    ClassB::ClassB(void* handle)
    {
        selfPtr = handle;
    }
    
    int ClassB::get_MyProperty()
    {
        return _MyProperty;
        auto ret = cbg_ClassB_GetMyProperty(selfPtr);
        return ret;
    }
    void ClassB::set_MyProperty(int value)
    {
        _MyProperty = value;
        cbg_ClassB_SetMyProperty(selfPtr, value);
    }
    
    ClassB::ClassB(bool calledByDerived)
    {
        // Dummy function.
    }
    
    ClassB::ClassB()
    {
        selfPtr = cbg_ClassB_Constructor_0();
    }
    
    void ClassB::SetValue(float value)
    {
        cbg_ClassB_SetValue(selfPtr, value);
    }
    
    void ClassB::SetEnum(Animal enumValue)
    {
        cbg_ClassB_SetEnum(selfPtr, (int)enumValue);
    }
    
    Animal ClassB::GetEnum(int id)
    {
        auto ret = cbg_ClassB_GetEnum(selfPtr, id);
        return (Animal)ret;
    }
    
    ClassB::~ClassB()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_ClassB_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
    std::mutex ClassC::mtx;
    
    std::unordered_map<void*, std::weak_ptr<ClassC> > ClassC::cacheRepo;
    std::shared_ptr<ClassC> ClassC::TryGetFromCache(void* native)
    {
        if(native == nullptr) return nullptr;
        
        if(cacheRepo.count(native))
        {
            std::shared_ptr<ClassC> cacheRet = cacheRepo[native].lock();
            if(cacheRet.get() != nullptr)
            {
                cbg_ClassC_Release(native);
                return cacheRet;
            }
            else
            {
                if(cacheRepo.count(native)) cacheRepo.erase(native);
            }
        }
        
        std::shared_ptr<ClassC> newObject(new ClassC(native));
        if(!cacheRepo.count(native)) cacheRepo[native] = newObject;
        return newObject;
    }
    
    
    void* ClassC::cbg_ClassC_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_Constructor_0");
        return proc();
    }
    
    void ClassC::cbg_ClassC_SetValue(void* selfPtr, float value)
    {
        typedef void (*proc_t)(void* selfPtr, float value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_SetValue");
        proc(selfPtr, value);
    }
    
    void ClassC::cbg_ClassC_SetEnum(void* selfPtr, int enumValue)
    {
        typedef void (*proc_t)(void* selfPtr, int enumValue);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_SetEnum");
        proc(selfPtr, enumValue);
    }
    
    int ClassC::cbg_ClassC_GetEnum(void* selfPtr, int id)
    {
        typedef int (*proc_t)(void* selfPtr, int id);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_GetEnum");
        return proc(selfPtr, id);
    }
    
    void ClassC::cbg_ClassC_FuncHasRefArg(void* selfPtr, int* intRef)
    {
        typedef void (*proc_t)(void* selfPtr, int* intRef);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_FuncHasRefArg");
        proc(selfPtr, intRef);
    }
    
    int ClassC::cbg_ClassC_GetMyProperty(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_GetMyProperty");
        return proc(selfPtr);
    }
    
    void ClassC::cbg_ClassC_SetMyProperty(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_SetMyProperty");
        proc(selfPtr, value);
    }
    
    const char16_t* ClassC::cbg_ClassC_GetStringProperty(void* selfPtr)
    {
        typedef const char16_t* (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_GetStringProperty");
        return proc(selfPtr);
    }
    
    void ClassC::cbg_ClassC_SetStringProperty(void* selfPtr, const char16_t* value)
    {
        typedef void (*proc_t)(void* selfPtr, const char16_t* value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_SetStringProperty");
        proc(selfPtr, value);
    }
    
    void ClassC::cbg_ClassC_SetMyBool(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_SetMyBool");
        proc(selfPtr, value);
    }
    
    void ClassC::cbg_ClassC_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_AddRef");
        proc(selfPtr);
    }
    
    void ClassC::cbg_ClassC_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_ClassC_Release");
        proc(selfPtr);
    }
    
    ClassC::ClassC(void* handle)
    {
        selfPtr = handle;
    }
    
    int ClassC::get_MyProperty()
    {
        return _MyProperty;
        auto ret = cbg_ClassC_GetMyProperty(selfPtr);
        return ret;
    }
    void ClassC::set_MyProperty(int value)
    {
        _MyProperty = value;
        cbg_ClassC_SetMyProperty(selfPtr, value);
    }
    
    std::basic_string<char16_t> ClassC::get_StringProperty()
    {
        return _StringProperty;
        auto ret = cbg_ClassC_GetStringProperty(selfPtr);
        return ret;
    }
    void ClassC::set_StringProperty(std::basic_string<char16_t> value)
    {
        _StringProperty = value;
        cbg_ClassC_SetStringProperty(selfPtr, value.c_str());
    }
    
    
    void ClassC::set_MyBool(bool value)
    {
        cbg_ClassC_SetMyBool(selfPtr, value);
    }
    
    ClassC::ClassC(bool calledByDerived)
    {
        // Dummy function.
    }
    
    ClassC::ClassC()
    {
        selfPtr = cbg_ClassC_Constructor_0();
    }
    
    void ClassC::SetValue(float value)
    {
        cbg_ClassC_SetValue(selfPtr, value);
    }
    
    void ClassC::SetEnum(Animal enumValue)
    {
        cbg_ClassC_SetEnum(selfPtr, (int)enumValue);
    }
    
    Animal ClassC::GetEnum(int id)
    {
        auto ret = cbg_ClassC_GetEnum(selfPtr, id);
        return (Animal)ret;
    }
    
    void ClassC::FuncHasRefArg(std::shared_ptr<int> intRef)
    {
        cbg_ClassC_FuncHasRefArg(selfPtr, intRef.get());
    }
    
    ClassC::~ClassC()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_ClassC_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
    std::mutex BaseClass::mtx;
    
    std::unordered_map<void*, std::weak_ptr<BaseClass> > BaseClass::cacheRepo;
    
    void* BaseClass::cbg_BaseClass_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_BaseClass_Constructor_0");
        return proc();
    }
    
    int BaseClass::cbg_BaseClass_GetBaseClassField(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_BaseClass_GetBaseClassField");
        return proc(selfPtr);
    }
    
    void BaseClass::cbg_BaseClass_SetBaseClassField(void* selfPtr, int value)
    {
        typedef void (*proc_t)(void* selfPtr, int value);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_BaseClass_SetBaseClassField");
        proc(selfPtr, value);
    }
    
    void BaseClass::cbg_BaseClass_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_BaseClass_AddRef");
        proc(selfPtr);
    }
    
    void BaseClass::cbg_BaseClass_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_BaseClass_Release");
        proc(selfPtr);
    }
    
    BaseClass::BaseClass(void* handle)
    {
        selfPtr = handle;
    }
    
    BaseClass::BaseClass(bool calledByDerived)
    {
        // Dummy function.
    }
    
    BaseClass::BaseClass()
    {
        selfPtr = cbg_BaseClass_Constructor_0();
    }
    
    int BaseClass::GetBaseClassField()
    {
        auto ret = cbg_BaseClass_GetBaseClassField(selfPtr);
        return ret;
    }
    
    void BaseClass::SetBaseClassField(int value)
    {
        cbg_BaseClass_SetBaseClassField(selfPtr, value);
    }
    
    BaseClass::~BaseClass()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_BaseClass_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
    std::mutex DerivedClass::mtx;
    
    std::unordered_map<void*, std::weak_ptr<DerivedClass> > DerivedClass::cacheRepo;
    
    void* DerivedClass::cbg_DerivedClass_Constructor_0()
    {
        typedef void* (*proc_t)();
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_DerivedClass_Constructor_0");
        return proc();
    }
    
    int DerivedClass::cbg_DerivedClass_GetBaseClassFieldFromDerivedClass(void* selfPtr)
    {
        typedef int (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_DerivedClass_GetBaseClassFieldFromDerivedClass");
        return proc(selfPtr);
    }
    
    void DerivedClass::cbg_DerivedClass_AddRef(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_DerivedClass_AddRef");
        proc(selfPtr);
    }
    
    void DerivedClass::cbg_DerivedClass_Release(void* selfPtr)
    {
        typedef void (*proc_t)(void* selfPtr);
        static proc_t proc = GetLibrary()->GetProc<proc_t>("cbg_DerivedClass_Release");
        proc(selfPtr);
    }
    
    DerivedClass::DerivedClass(void* handle) : BaseClass(handle)
    {
        selfPtr = handle;
    }
    
    DerivedClass::DerivedClass(bool calledByDerived) : BaseClass(calledByDerived)
    {
        // Dummy function.
    }
    
    DerivedClass::DerivedClass() : BaseClass(true)
    {
        selfPtr = cbg_DerivedClass_Constructor_0();
    }
    
    int DerivedClass::GetBaseClassFieldFromDerivedClass()
    {
        auto ret = cbg_DerivedClass_GetBaseClassFieldFromDerivedClass(selfPtr);
        return ret;
    }
    
    DerivedClass::~DerivedClass()
    {
        std::lock_guard<std::mutex> lock(mtx);
        if (selfPtr != nullptr)
        {
            cbg_DerivedClass_Release(selfPtr);
            selfPtr = nullptr;
        }
    }
    
}
