using System;

using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using Client.models;


namespace Client.commands
{
  class AddAllergiesCommand : ACommand
  {

    public AddAllergiesCommand()
    {
      name = "addAllergies";
      description = "add allergies to the given user";
      nb_parameters = 2;
      parameters = "<userID> <allergy_1> <allergy_2> ... <allergy_n>";
      options = new List<Option>();

    }

    public AddAllergiesCommand(String[] args, String[] options) : this()
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
      IUserProfil service = new UserProfilClient(); ;
      Console.WriteLine("Submitting allergies...");
      System.Threading.Thread.Sleep(1000);
      service.inquirePreferences(args);
      Console.WriteLine("Successefully added!");
      JObject response = JObject.Parse(service.inquireAllergies(args));
      JArray jArray = (JArray)response["items"];
      if (jArray.Count != 0)
      {
        Console.Write("Except for the following items that does not exist and thus cannot be added as allergies : ");
        for (int i = 0; i < jArray.Count; i++)
        {
          Console.Write(jArray[i] + (i == (jArray.Count - 1) ? "" : ","));

        }
        Console.WriteLine("\n");
      }
      return false;

    }
  }
}
