using System;
using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using Client.models;

using System.Collections.Generic;





namespace Client.commands
{
  class RemoveFromFridgeCommand : ACommand
  {


    public RemoveFromFridgeCommand()
    {
      this.name = "removeFromFridge";
      this.parameters = "<userID> <ingredient_1> <Ingredient_2> ... <Ingredient_n>";
      this.description = "remove the given ingredients from the users's fridge";
      this.nb_parameters = 2;
      options = new List<Option>();


    }

    public RemoveFromFridgeCommand(String[] args, String[] options) : this()
    {
      this.args = args;
      activated_options = options;

    }

    protected override bool fixedParameters()
    {
      return false;
    }

    protected override bool run()
    {
      Console.WriteLine("Removing from fridge...");
      System.Threading.Thread.Sleep(1000);
      IUserProfil service = new UserProfilClient();
      JObject j = JObject.Parse(service.removePreferences(args));
      Console.WriteLine("Successefully removed!");
      JArray jArray = (JArray)j["items"];
      if (jArray.Count != 0) {
        Console.WriteLine("Except " +  (jArray.Count > 1 ?   "those items that are not " : "this item that is not") + " in your fridge and thus does not need to be removed :");
        for (int i = 0; i < jArray.Count; i++)
        {
          Console.Write(jArray[i] + " " + (i == (jArray.Count - 1) ? "" : ","));
        }
        Console.WriteLine("\n");
      }

    
      return false;
    }






  }
}
