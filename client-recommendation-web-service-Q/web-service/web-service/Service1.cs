using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.IO;
using System.Net;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;



namespace web_service
{
  // REMARQUE : vous pouvez utiliser la commande Renommer du menu Refactoriser pour changer le nom de classe "Service1" à la fois dans le code et le fichier de configuration.
  public class Service1 : IService1
  {

    string url = "http://127.0.0.1:8282";

    public string GetData(int value)
    {
      return string.Format("You entered: {0}", value);
    }

    private String generateResponse(string url, JObject j)
    {
      WebRequest webRequest = WebRequest.Create(url);
      webRequest.Method = "POST";
      webRequest.ContentType = "application/json;charset=UTF-8";
      StreamWriter requestWriter = new StreamWriter(webRequest.GetRequestStream());
      requestWriter.Write(j);
      requestWriter.Close();
      WebResponse response = webRequest.GetResponse();
      StreamReader reader = new StreamReader(response.GetResponseStream());
      String res = reader.ReadToEnd();

      System.Diagnostics.Debug.WriteLine("#############################################");
      System.Diagnostics.Debug.WriteLine("Res = " + res);
      System.Diagnostics.Debug.WriteLine("#############################################");
      return res;
    }

    public string getRecommendations(string[] args, Boolean fridge)
    {

      JObject j = new JObject();
      j["users"] = new JArray(args);
      j["fridge"] = fridge.ToString() ;
      url += "/getRecommendation";
      WebRequest webRequest = WebRequest.Create(url);
      webRequest.Method = "POST";
      webRequest.ContentType = "application/json;charset=UTF-8";
      StreamWriter requestWriter = new StreamWriter(webRequest.GetRequestStream());
      requestWriter.Write(j);
      requestWriter.Close();
      WebResponse response = webRequest.GetResponse();
      StreamReader reader = new StreamReader(response.GetResponseStream());
      String res = reader.ReadToEnd();
      JArray responseJson = JArray.Parse(res);
      System.Diagnostics.Debug.WriteLine(responseJson);
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);


    }

    public string evaluateRecipe(string[] args)
    {
      JObject j = new JObject();
      j["userID"] = args[0];
      j["recipeID"] = args[1];
      j["rate"] = args[2];

      url += "/evaluateRecipe";

      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("The recipe " + args[1] + " has been rated by the user " + args[0]);
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }





  }
}
