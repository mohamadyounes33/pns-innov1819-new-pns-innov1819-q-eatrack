using System;
using Client.ServiceReference2;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using Client.models;



namespace Client.commands
{
  class EmptyFridgeCommand : ACommand
  {
    public EmptyFridgeCommand()
    {
      name = "emptyFridge";
      parameters = "<userID>";
      nb_parameters = 1;
      description = "empty the user's fridge";
      options = new List<Option>();

    }

    public EmptyFridgeCommand(String[] args, String[] options) : this()
    {
      this.args = args;
      activated_options = options;

    }


    protected override bool run()
    {
      Console.WriteLine("Emptying fridge...");
      IUserProfil service = new UserProfilClient();
      JObject j = JObject.Parse(service.emptyFridge(args));
      Console.WriteLine("Your fridge is now empty");
      return false;

    }
  }
}
