using System;
using System.Collections.Generic;
using Client.models;



namespace Client
{
  class QuitCommand : ACommand
  {


    public QuitCommand()
    {
      name = "quit";
      description = "exit Eatrack";
      nb_parameters = 0;
      options = new List<Option>();

    }
    public QuitCommand(String[] args, String[] options) : this()
    {
      base.args = args;
      activated_options = options;

    }

    protected override Boolean run()
    {
      Console.WriteLine("Exiting Eatrack ...");
      Console.WriteLine("See you soon ;)");
      System.Threading.Thread.Sleep(2000);
      return true;
    }


  }
}
