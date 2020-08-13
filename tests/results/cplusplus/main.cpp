#include <iostream>
#include <memory>
#include <string>

#include "AutoGeneratedCoreBindings.h"

int main()
{
    HelloWorldA::LoadLibrary();

    auto a = std::shared_ptr<HelloWorldA::ClassA>(new HelloWorldA::ClassA());
    a->FuncSimple();
    a->FuncArgInt(2);
    a->FuncArgFloatBoolStr(2.2f, true, u"hello");

    if(HelloWorldA::ClassA::FuncReturnStatic() != 1)
        throw "Process call failed : HelloWorld::ClassA::FuncReturnStatic()";

    a->set_EnumA(HelloWorldA::Animal::Tiger);
    if(a->get_EnumA() != HelloWorldA::Animal::Tiger)
        throw "Process call failed : HelloWorld::ClassA::get_EnumA()";

    HelloWorldA::StructA_C *sa = new HelloWorldA::StructA_C();
    sa->X = 1.0f;
    sa->Y = 2.0f;
    sa->Z = 3.0f;
    a->FuncArgStruct(std::shared_ptr<HelloWorldA::StructA_C>(sa));

    auto cb = std::shared_ptr<HelloWorldA::ClassB>(new HelloWorldA::ClassB());
    cb->SetValue(100);
    a->FuncArgClass(cb);

    auto retBool = a->FuncReturnBool();
    std::cout << "retBool:" << (retBool ? "true" : "false") << std::endl;

    auto retStruct = a->FuncReturnStruct();
    std::cout << "retStruct(should 2, 1, 3):"
        << retStruct.X << ", " << retStruct.Y << ", " << retStruct.Z << std::endl;

    auto retString = a->FuncReturnString();
    std::cout << retString.c_str() << std::endl;

    auto retClass = a->FuncReturnClass();
    retClass->SetValue(101);
    a->FuncArgClass(retClass);

    std::cout << "Inheritance Test:" << std::endl;
    auto derived = std::shared_ptr<HelloWorldA::DerivedClass>(new HelloWorldA::DerivedClass());
    auto asBase = std::static_pointer_cast<HelloWorldA::BaseClass>(derived);
    asBase->SetBaseClassField(12345);
    std::cout << "As Base Value:" << asBase->GetBaseClassField() << std::endl;
    std::cout << "Derived Value:" << derived->GetBaseClassFieldFromDerivedClass() << std::endl;
}