using System;
using System.Collections.Generic;
using System.Linq;
using Client.models;



namespace Client
{
  class MenuCommand : ACommand
  {
    public MenuCommand(){
      name = "?";
      options = new List<Option>();


    }

    public MenuCommand(String[] args, String[] options) : this()
    {
      base.args = args;
      activated_options = options;

    }

    protected override Boolean run()
    {
      Console.WriteLine("Commands available :");

      List<ACommand> all_commands = getCommands();
      foreach(ACommand aCommand in all_commands)
      {
        Console.WriteLine(aCommand.ToString());
      }
      return false;
    }

    private List<ACommand> getCommands()
    {
      List<Type> allSubTypes = new List<Type>();
      List<ACommand> commands = new List<ACommand>();
      foreach (var assem in AppDomain.CurrentDomain.GetAssemblies())
      {
        var subTypes = assem.GetTypes().Where(x => x.BaseType == typeof(ACommand) && x != typeof(MenuCommand));

        allSubTypes.AddRange(subTypes);
      }
      foreach (var type in allSubTypes)
      {
        ACommand instance = (ACommand)Activator.CreateInstance(type);
        commands.Add(instance);
      }

      return commands;
    }

  }
    
}
