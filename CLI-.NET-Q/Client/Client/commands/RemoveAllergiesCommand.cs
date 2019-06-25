using System;

using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using Client.models;

using System.Collections.Generic;


namespace Client.commands
{
  class RemoveAllergiesCommand : ACommand
  {
    public RemoveAllergiesCommand()
    {
      name = "removeAllergies";
      description = "remove allergies from the given user";
      nb_parameters = 2;
      parameters = "<userID> <allergy_1> <allergy_2> ... <allergy_n>";
      options = new List<Option>();

    }

    public RemoveAllergiesCommand(String[] args, String[] options) : this()
    {
      activated_options = options;
      this.args = args;
    }

    protected override bool fixedParameters()
    {
      return false;
    }

    protected override bool run()
    {
      IUserProfil service = new UserProfilClient();;
      Console.WriteLine("Removing allergies...");
      System.Threading.Thread.Sleep(1000);
      service.inquirePreferences(args);
      Console.WriteLine("Successefully removed!");
      JObject response = JObject.Parse(service.removeAllergies(args));
      JArray jArray = (JArray)response["items"];
      if (jArray.Count != 0)
      {
        Console.Write("Except for the following items that does not exist and thus cannot be removed : ");
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
