using UnityEngine;
using UnityEngine.UI;

public class PropertyInfo : MonoBehaviour
{
    public Text titleText;
    public Text descriptionText;
    public Text priceText;

    public void SetInfo(string title, string description, float price)
    {
        titleText.text = title;
        descriptionText.text = description;
        priceText.text = "Price: $" + price.ToString("F2");
    }
}
