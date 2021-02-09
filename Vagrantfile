Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network :public_network, ip: "192.168.1.230", :bridge => 'wlp3s0'
  #config.vm.network "forwarded_port", guest: 80, host: 8080#, protocol: "udp", auto_correct: true
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
