Configuration management
------------------------

Puppet is a popular configuration management (CM) tool that automates the management of infrastructure and applications. It uses `declarative code` to define the desired state of systems and ensures they stay in that state.

## How puppet works

### Master-Agent Model:

- Puppet Master: The central server that contains the configuration rules (manifests).
- Puppet Agents: The nodes (e.g., servers, devices) that apply these rules to configure themselves.
- Agents communicate with the Master to pull the latest configurations.

### Puppet Language:

- Uses a domain-specific language (DSL) written in Ruby to define the desired state of the system in files called `manifests`.
- Example: Install Apache, set file permissions, or ensure a service is running.

### Idempotence:

- If a system is already in the desired state, Puppet does nothing, avoiding redundant actions.

## Key Components

### Manifests:

- Files that describe the desired configuration using Puppet's DSL.

- Example:
```puppet
package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
}
```

### Modules:

- Collections of manifests, files, templates, and other resources grouped to manage specific applications or systems.

### Catalog:

- A compiled version of manifests sent to the Puppet Agent, describing how the system should look.

### Resources:

- The building blocks of configurations (e.g., files, packages, services).

### Facter:

- A tool that gathers system information (facts) like OS, IP address, or hostname, which Puppet can use in its manifests.

### Hiera:

- A key-value lookup tool that allows you to separate data (like configurations) from code.

