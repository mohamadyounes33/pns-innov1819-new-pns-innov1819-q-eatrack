using System;
using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using Client.models;



namespace Client.commands
{
  class AddPreferencesCommand : ACommand
  {

    public AddPreferencesCommand()
    {
      name = "addPrefs";
      description = "add preferences to the given user";
      nb_parameters = 2;
      parameters = "<userID> <pref_1> <pref_2> ... <pref_n>";
      options = new List<Option>();

    }

    public AddPreferencesCommand(String[] args, String[] options) : this()
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
      Console.WriteLine("Submitting preferences...");
      System.Threading.Thread.Sleep(1000);
      service.inquirePreferences(args);
      Console.WriteLine("Successefully added!");
      JObject response = JObject.Parse(service.inquirePreferences(args));
      JArray jArray = (JArray)response["items"];
      if(jArray.Count != 0)
      {
        Console.Write("Except for the following items that does not exist and thus cannot be added as preferences : ");
        for(int i = 0; i < jArray.Count; i++)
        {
          Console.Write(jArray[i] + (i == (jArray.Count - 1) ? "" : ","));

        }
        Console.WriteLine("\n");
      }
      return false;

    }

  }
}
