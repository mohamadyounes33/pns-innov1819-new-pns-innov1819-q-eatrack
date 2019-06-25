using System;
using Client.exceptions;
using Client.commands;

namespace Client
{
  class CommandFactory
  {
    public CommandFactory()
    {
    }
    public ACommand createCommand(String command, String[]args, String[] options)
    {
      if (command.Equals("getrec"))
      {
        return new GetRecommendationCommand(args, options);
      }
      if (command.Equals("getusers"))
      {
        return new GetUsersCommand(args, options);
      }
      if (command.Equals("quit"))
      {
        return new QuitCommand(args, options);
      }
      if (command.Equals("?"))
      {
        return new MenuCommand(args, options);
      }
      if (command.Equals("raterecipe"))
      {
        return new RateRecipeCommand(args, options);
      }
      if (command.Equals("addToFridge"))
      {
        return new AddToFridgeCommand(args, options);
      }
      if (command.Equals("removeFromFridge"))
      {
        return new RemoveFromFridgeCommand(args, options);
      }
      throw new CommandUnknowknException();

    }
  }
}
