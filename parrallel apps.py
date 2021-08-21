#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Going to settings and opening 
import uiautomator2 as u2
import time
d=u2.connect('66be464c')
d.unlock()
d.press('home')
d(text="1").click()
d(text="2").click()
d(text="3").click()
d(text="4").click()
time.sleep(2)
d.open_quick_settings()
time.sleep(1)
d(className="android.widget.ImageButton",resourceId="com.android.systemui:id/settings_button").click()
time.sleep(1)
d.press('down')
d.press('down')
d.press('down')
d.press('down')
time.sleep(1)
d(text="Utilities").click()
time.sleep(1)
d(text='Parallel Apps').click()
d(text='Facebook').click()
time.sleep(2)
d(text='Messenger').click()
d.press('home')
time.sleep(1)
d(className="android.widget.ImageView",resourceId="net.oneplus.launcher:id/page_indicator_caret").click()
time.sleep(2)
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d.press('down')
time.sleep(1)
d(text='Facebook').click()
time.sleep(1)
d.press('home')
d(className="android.widget.ImageView",resourceId="net.oneplus.launcher:id/page_indicator_caret").click()
time.sleep(2)
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d.press('down')
d(className="android.widget.TextView",resourceId="net.oneplus.launcher:id/icon").click()
time.sleep(2)
d.press('home')



  




# In[43]:


d.press('up')
d.press('up')


# In[49]:


d(className="android.widget.TextView",resourceId="net.oneplus.launcher").click()


# In[ ]:




