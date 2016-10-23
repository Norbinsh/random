https://github.com/spikenode/DevOps-Interview-Questions#contributors


# General


### Have you used Puppet, Chef, Salt or Ansible?
Not yet.
### How long have you used it for?
### Have you used it in production?
### Describe the size of the environment that you automated (how many servers, small scale or large scale)
### Describe the most challenging situation that you were faced with and how did you fix it?


# Network Questions


### What’s a PTR in DNS?
A record of type == PTR, that is used to look up a domain name by IP, quite the opposite of an A record.

Using a special domain (in IPV4 at least): 'in-addr-arpa', for example:

For google's DNS server: 8.8.4.4, let's find the PTR record:

shay@redbox:~$ dig -x 8.8.4.4

ANSWER: 4.4.8.8.in-addr.arpa. PTR google-public-dns-b.google.com. -> 8.8.4.4

### What’s a MX record in DNS?
Helps with the domain's mail flow by directing the sender to the appropriate mailserver we have configured.
### How a CDN chooses the closest host to serve a client?
A possible way would be by looking up a data base and understanding where the IP range of the request is coming from
in the world, and then serving that request from your nearest data center.
### In which cases would you choose to not implement a CDN?
Possibly with a complex enough application that can't have its files changed in *any* way.
When data is too sensitive and is not to be routed through anyone else, not even a trusted CDN.
When a possible latency addition is possible due to extra routes.


# Linux Questions


### Difference between RAID 0, 1 and 5?
RAID 0 is active-active mode, all disks share/read-write at the same time, in case and one of them goes corrupt, there's
big risk of partial or complete data loss. Great performance however.

IN RAID 5, each block device stores the same data as the other, which is good for redundancy.

Performance wise, read requests are served by all blocks, which helps.

In case and one disk goes bad, others will keep serving data.

### What’s the advantage of one RAID over another?

Raid 0 Pros: Performance

Raid 0 Cons: Redundancy

Raid 5 Pros: Reliable, somewhat better than most read performance.

Raid 5 Cons: Write speeds not as fast as Raid 0.

### Alternative to init.d in Linux?
Systemd!
How to view running processes in Linux?
ps, ps aux, etc.
How to check DNS records in Linux?
dig em.


