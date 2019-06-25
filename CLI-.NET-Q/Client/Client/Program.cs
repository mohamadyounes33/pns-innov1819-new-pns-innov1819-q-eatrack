using System;
using System.Collections.Generic;
using System.Linq;




namespace Client
{
  class Program
  {


    static void Main()

    {

      Program p = new Program();
      CommandFactory commandFactory = new CommandFactory();
      p.StartApplication();
      Boolean quit = false;
      while (!quit)
      {
        Console.Write("> ");
        string[] input_array = Console.ReadLine().Trim().Split(' ');
        string command = input_array[0];
        List<string> args = new List<string>();
        List<string> options = new List<string>();
        input_array = input_array.Skip(1).ToArray();
        foreach(string s in input_array)
        {
          if(s[0] == '-')
          {
            options.Add(s);
          }
          else
          {
            args.Add(s);
          }
        }
        ACommand the_command;
        try
        {
          the_command = commandFactory.createCommand(command, args.ToArray(), options.ToArray());
          quit = the_command.execute();

        }
        catch (Exception e)
        {
          System.Console.WriteLine(e.Message);
        }
      }

    }
    public void StartApplication()
    {
      Console.WriteLine("Starting Eatrack...");
      System.Threading.Thread.Sleep(2000);
      Console.WriteLine("WELCOME TO EATRACK!");
      Console.WriteLine("Use Eatrack to get recipes recommendations");
      Console.WriteLine("type '?' to see the commands available");
    }






  }
}
