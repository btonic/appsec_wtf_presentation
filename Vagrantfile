# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"


  config.vm.define :redis_takeover do |takeover|
    takeover.vm.network "private_network", type: "dhcp"
    # Update the apt repositories before other installations occur
    takeover.vm.provision :shell, inline: "apt-get update"

    ############################################################################
    # Services
    ############################################################################
    # Install Redis
    takeover.vm.provision :shell, path: "vagrant/services/redis/install.sh"
  end
  config.vm.define :wtf_app do |wtf_app|
    ############################################################################
    # Networking
    ############################################################################
    # Port forward the default wtf app
    wtf_app.vm.network "forwarded_port", guest: 3000, host: 3000
    # Port forward the callback server
    wtf_app.vm.network "forwarded_port", guest: 8000, host: 8000
    # Connect this VM to the redis_takeover vm
    wtf_app.vm.network "private_network", type: "dhcp"

    
    # Update the apt repositories before other installations occur
    wtf_app.vm.provision :shell, inline: "apt-get update"

    ############################################################################
    # Services
    ############################################################################
    # Install Redis
    wtf_app.vm.provision :shell, path: "vagrant/services/redis/install.sh"

    ############################################################################
    # Python configuration & module installation
    ############################################################################

    # Install pip & virtualenvwrapper
    wtf_app.vm.provision :shell, path: "vagrant/environment/python/install_deps.sh"
    # Configure the shell to automatically load into the virtualenv environment
    wtf_app.vm.provision :shell, path: "vagrant/environment/python/configure_default.sh", privileged: false
    # Install the application as the default SSH user
    wtf_app.vm.provision :shell, path: "vagrant/environment/appsec_wtf/install.sh", privileged: false

    ############################################################################
    # Tool installation
    ############################################################################
    # Install nmap
    wtf_app.vm.provision :shell, path: "vagrant/tools/nmap/install.sh"
  end
end
