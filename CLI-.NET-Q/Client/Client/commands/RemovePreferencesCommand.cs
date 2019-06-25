using System;
using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using Client.models;

using System.Collections.Generic;

namespace Client.commands
{
  class RemovePreferencesCommand : ACommand
  {

    public RemovePreferencesCommand()
    {
      name = "removePrefs";
      description = "remove the given preferences from the user";
      parameters = "<userID> <pref_1> <pref_2> ... <pref_n>";
      nb_parameters = 2;
      options = new List<Option>();


    }

    public RemovePreferencesCommand(String[] args, String[] options) : this() {
      this.args = args;
      activated_options = options;
    }

    protected override bool fixedParameters()
    {
      return false;
    }

    protected override bool run()
    {
      Console.WriteLine("Removing preferences...");
      System.Threading.Thread.Sleep(1000);
      IUserProfil service = new UserProfilClient();
      JObject j = JObject.Parse(service.removePreferences(args));
      Console.WriteLine("Successefully removed");
      JArray array = (JArray)j["items"];
      if(array.Count != 0)
      {
        Console.Write("Except the following items that does not exist : ");
        for(int i = 0; i < array.Count; i++)
        {
          Console.Write(array[i] + (i == (array.Count - 1) ? "" : ","));
        }
        Console.WriteLine("\n");
      }
      return false;


    }
  }
}
