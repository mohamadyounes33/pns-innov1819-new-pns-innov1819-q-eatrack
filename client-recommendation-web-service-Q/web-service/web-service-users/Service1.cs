using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.IO;
using System.Net;
using Newtonsoft.Json.Linq;

namespace web_service_users
{
  // REMARQUE : vous pouvez utiliser la commande Renommer du menu Refactoriser pour changer le nom de classe "Service1" à la fois dans le code et le fichier de configuration.
  public class Service1 : IUserProfil
  {
    string url = "http://127.0.0.1:8080";

    private String generateResponse(string url, JObject j)
    {
      WebRequest webRequest = WebRequest.Create(url);
      webRequest.Method = "POST";
      webRequest.ContentType = "application/json;charset=UTF-8";
      if(j != null)
      {
        StreamWriter requestWriter = new StreamWriter(webRequest.GetRequestStream());
        requestWriter.Write(j);
        requestWriter.Close();
      }
      WebResponse response = webRequest.GetResponse();
      StreamReader reader = new StreamReader(response.GetResponseStream());
      String res = reader.ReadToEnd();

      System.Diagnostics.Debug.WriteLine("#############################################");
      System.Diagnostics.Debug.WriteLine("Res = " + res);
      System.Diagnostics.Debug.WriteLine("#############################################");
      return res;
    }


    public string inquirePreferences(string[] args)
    {
      JObject j = new JObject();
      j["userID"] = args[0];
      j["preferences"] = new JArray(args.Skip(1).ToArray());

      url += "/inquirePreferences";
      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("inquirePreferences");
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }

    public string removePreferences(string[] args)
    {
      JObject j = new JObject();
      j["userID"] = args[0];
      j["preferences"] = new JArray(args.Skip(1).ToArray());

      url += "/removePreferences";

      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("removePreferences");
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }

    public string inquireAllergies(string[] args)
    {
      JObject j = new JObject();
      j["userID"] = args[0];
      j["allergies"] = new JArray(args.Skip(1).ToArray());

      url += "/inquireAllergies";
      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("inquireAllergies");
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }

    public string removeAllergies(string[] args)
    {
      JObject j = new JObject();
      j["userID"] = args[0];
      j["allergies"] = new JArray(args.Skip(1).ToArray());

      url += "/removeAllergies";

      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("removeAllergies");
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }

    public string addToFridge(string[] args)
    {
      url = url + "/addToFridge";
      JObject j = new JObject();
      JArray jarray = new JArray(args.Skip(1).ToArray());
      j["items"] = jarray;
      j["userID"] = args[0];
      JObject responseJson = JObject.Parse(generateResponse(url, j));
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }

    public string removeFromFridge(string[] args)
    {
      url += "/removeFromFridge";
      JObject j = new JObject();
      JArray jarray = new JArray(args.Skip(1).ToArray());
      j["items"] = jarray;
      j["userID"] = args[0];
      JObject responseJson = JObject.Parse(generateResponse(url, j));
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);
    }

    public string emptyFridge(string[] args)
    {
      url += "/emptyFridge";
      JObject j = new JObject();
      j["userID"] = args[0];
      JObject responseJson = JObject.Parse(generateResponse(url, j));
      System.Diagnostics.Debug.WriteLine("emptyFridge");
      return responseJson.ToString(Newtonsoft.Json.Formatting.None);

    }



  }
}
