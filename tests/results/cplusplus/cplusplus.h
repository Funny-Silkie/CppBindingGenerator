
#pragma once

#include <memory>

#include "AutoGeneratedCoreBindings.h"

namespace HelloWorldCpp
{
	class ReferenceObject
	{
		int ref = 1;

	public:
		ReferenceObject() = default;
		virtual ~ReferenceObject() = default;

		int AddRef()
		{
			ref++;
			return ref;
		}

		int Release()
		{
			ref--;
			auto ret = ref;
			if (ref == 0)
			{
				delete this;
			}
			return ret;
		}
	};

	template <typename T>
	struct ReferenceDeleter
	{
		void operator()(T* p)
		{
			if (p != nullptr)
			{
				p->Release();
				p = nullptr;
			}
		}
	};

	template <class T>
	std::shared_ptr<T> CreateAndAddSharedPtr(T* p)
	{
		if (p == nullptr)
			return nullptr;

		p->AddRef();
		return std::shared_ptr<T>(p, ReferenceDeleter<T>());
	}

	template <class T>
	T* AddAndGetSharedPtr(std::shared_ptr<T> sp)
	{
		auto p = sp.get();
		if (p == nullptr)
			return nullptr;

		p->AddRef();
		return p;
	}

	template <class T>
	std::shared_ptr<T> CreateAndAddSharedPtr_Dependence(void** p)
	{
		if (p == nullptr)
			return nullptr;

		T::AddRef(p);
		return std::shared_ptr<T>(p, T::CreateFromCache(p));
	}

	template <class T>
	void* AddAndGetSharedPtr_Dependence(std::shared_ptr<T> sp)
	{
		auto p = sp->GetInternal();
		if (p == nullptr)
			return nullptr;

		T::AddRef(p);
		return p;
	}

	class ClassCppD : public ReferenceObject
	{
	public:
		std::shared_ptr<HelloWorldA::ClassB> FuncReturnClass() {
			auto v = new HelloWorldA::ClassB();
			return std::shared_ptr<HelloWorldA::ClassB>(v);
		}
	};

} // namespace HelloWorldCpp