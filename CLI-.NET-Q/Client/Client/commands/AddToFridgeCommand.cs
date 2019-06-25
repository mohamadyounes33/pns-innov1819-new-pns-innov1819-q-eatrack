using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using Client.models;



namespace Client.commands
{
  class AddToFridgeCommand : ACommand
  {
    public AddToFridgeCommand()
    {
      name = "addToFridge";
      description = "add the given ingredients to the user's fridge";
      parameters = "<userID> <ingredient_1> <ingredient_2> ... <ingredient_n>";
      nb_parameters = 2;
      options = new List<Option>();

    }

    public AddToFridgeCommand(String[] args, String[] options) : this()
    {
      this.args = args;
      activated_options = options;

    }

    protected override bool run()
    {
      IUserProfil service = new UserProfilClient(); ;
      JObject j = JObject.Parse(service.addToFridge(args));
      Console.WriteLine("Adding ingredients in the fridge...");
      System.Threading.Thread.Sleep(1000);
      service.addToFridge(args);
      Console.WriteLine("Successefully added!");
      JArray jarray = (JArray)j["items"];
      if (jarray.Count != 0)
      {
        Console.Write("Except the following items that does not exist : ");
        for (int i = 0; i < jarray.Count; i++)
        {
          Console.Write(jarray[i] + (i == (jarray.Count - 1) ? "" : ","));
        }
        Console.Write("\n");

      }
      return false;
    }

    protected override Boolean fixedParameters()
    {
      return false;
    }
  }
}
