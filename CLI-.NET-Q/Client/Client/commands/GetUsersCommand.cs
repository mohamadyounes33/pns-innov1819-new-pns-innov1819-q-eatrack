using System;
using Client.ServiceReference1;
using System.Collections.Generic;
using Client.models;



namespace Client
{
  class GetUsersCommand : ACommand
  {


    public GetUsersCommand()
    {
      name = "getusers";
      description = "get the list of the users";
      nb_parameters = 0;
      options = new List<Option>();

    }
    public GetUsersCommand(String[] args, String[] options) : this()
    {

      base.args = args;
      activated_options = options;

    }
    protected override Boolean run()
    {
      IService1 service = new Service1Client();
      return false;


    }

  }
}
