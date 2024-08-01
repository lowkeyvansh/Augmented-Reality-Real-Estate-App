using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class PropertyManager : MonoBehaviour
{
    public string apiUrl = "http://your-server-url/properties";
    public GameObject propertyPrefab;

    void Start()
    {
        StartCoroutine(GetProperties());
    }

    IEnumerator GetProperties()
    {
        UnityWebRequest www = UnityWebRequest.Get(apiUrl);
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            List<Property> properties = JsonUtility.FromJson<PropertyList>(www.downloadHandler.text).properties;
            foreach (Property prop in properties)
            {
                GameObject property = Instantiate(propertyPrefab, new Vector3(prop.latitude, 0, prop.longitude), Quaternion.identity);
                property.GetComponent<PropertyInfo>().SetInfo(prop.title, prop.description, prop.price);
            }
        }
    }
}

[System.Serializable]
public class Property
{
    public int id;
    public string title;
    public string description;
    public float price;
    public string image_file;
    public float latitude;
    public float longitude;
}

[System.Serializable]
public class PropertyList
{
    public List<Property> properties;
}
