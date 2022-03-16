#!/usr/bin/env python
# coding: utf-8

# In[5]:


from xml.dom import minidom  
xmldoc = minidom.parse('CHR2019.xml')
dataValueSets = xmldoc.getElementsByTagName('dataValueSet')
print(len(dataValueSets))
for dataValueSet in dataValueSets:
    print(dataValueSet.toxml()) 


# In[1]:


def callWoundcareAPI(requestData):
    from xml.dom import minidom
    import http.client
    conn = http.client.HTTPSConnection("woundinfo.us")
    xmldoc = minidom.parse(requestData)
    #print(xmldoc)
    dataValueSets = xmldoc.getElementsByTagName('dataValueSet')
    print(len(dataValueSets))
    for dataValueSet in dataValueSets:
        #print(bytearray(dataValueSet.toxml()), encoding='utf8')
        #print(xmldoc)
    
        headers = {
              'Authorization': 'Basic key',
              'Content-Type': 'application/xml'
        }

        #conn.request("POST", "/api/33/dataValueSets", xmldoc, headers)
        conn.request("POST", "/api/33/dataValueSets", dataValueSet.toxml(), headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8")) 


# In[2]:


callWoundcareAPI('savi2018.xml') 


# In[3]:


callWoundcareAPI('savi2019.xml') 


# In[ ]:





# In[6]:


def callWoundcareAPI(requestData):
    from xml.dom import minidom
    import http.client
    conn = http.client.HTTPSConnection("woundinfo.us")
    xmldoc = minidom.parse(requestData)
    #print(xmldoc)
    dataValueSets = xmldoc.getElementsByTagName('dataValueSet')
    print(len(dataValueSets))
    for dataValueSet in dataValueSets:
        #print(bytearray(dataValueSet.toxml()), encoding='utf8')
        #print(xmldoc)
    
        headers = {
              'Authorization': 'Basic key',
              'Content-Type': 'application/xml'
        }

        #conn.request("POST", "/api/33/dataValueSets", xmldoc, headers)
        conn.request("POST", "/api/33/dataValueSets", dataValueSet.toxml(), headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8")) 


# In[7]:


callWoundcareAPI('CHR2020.xml') 


# In[8]:


callWoundcareAPI('CHR2021.xml') 


# In[9]:


callWoundcareAPI('CHR2018.xml') 


# In[10]:


callWoundcareAPI('CHR2019.xml') 


# In[ ]:




