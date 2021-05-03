#!/usr/bin/env python
# coding: utf-8

# # 08 Module
# - 모듈은 함수나 변수 또는 클래스를 모아 놓은 파일

# In[91]:


class Calculator:
    class_var = 7
    def __init__(self):
        pass
    
    def set_data(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b


# In[92]:


cal1 = Calculator()
cal2 = Calculator()


# In[93]:


cal1.set_data(7,17)
cal1.class_var = 10


# In[94]:


cal2.set_data(17,7)


# In[97]:


print(cal1.a, cal2.a)
print(cal1.class_var, cal2.class_var, Calculator.class_var)


# In[102]:


Calculator.class_var = 22


# In[105]:


cal1.class_var


# In[ ]:




