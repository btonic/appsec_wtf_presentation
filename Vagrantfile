# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  ############################################################################
  # Networking
  ############################################################################
  # Port forward the default wtf app
  config.vm.network "forwarded_port", guest: 3000, host: 3000
  # Port forward the callback server
  config.vm.network "forwarded_port", guest: 8000, host: 8000


  # Update the apt repositories before other installations occur
  config.vm.provision :shell, inline: "apt-get update"

  ############################################################################
  # Services
  ############################################################################
  # Install Redis
  config.vm.provision :shell, path: "vagrant/services/redis/install.sh"

  ############################################################################
  # Python configuration & module installation
  ############################################################################

  # Install pip & virtualenvwrapper
  config.vm.provision :shell, path: "vagrant/environment/python/install_deps.sh"
  # Configure the shell to automatically load into the virtualenv environment
  config.vm.provision :shell, path: "vagrant/environment/python/configure_default.sh", privileged: false
  # Install the application as the default SSH user
  config.vm.provision :shell, path: "vagrant/environment/appsec_wtf/install.sh", privileged: false

  ############################################################################
  # Tool installation
  ############################################################################
  # Install nmap
  config.vm.provision :shell, path: "vagrant/tools/nmap/install.sh"
end
