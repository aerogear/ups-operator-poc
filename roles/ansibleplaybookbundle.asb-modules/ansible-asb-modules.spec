Name:           ansible-asb-modules
Version:        0.0.2
Release:        1%{?dist}
Summary:        Ansible role containing Ansible Service Broker modules
License:        ASL 2.0
URL:            https://github.com/ansibleplaybookbundle/%{name}
Source0:        https://github.com/ansibleplaybookbundle/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires: ansible >= 2.3.0.0

%description
%{summary}

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/ansible/roles/ansibleplaybookbundle.asb-modules
mv * %{buildroot}%{_sysconfdir}/ansible/roles/ansibleplaybookbundle.asb-modules

%check

%files
%{_sysconfdir}/ansible/roles/ansibleplaybookbundle.asb-modules

%changelog
* Thu Nov 02 2017 Jason Montleon <jmontleo@redhat.com> 0.0.2-1
- new package built with tito

* Fri May 12 2017 Chris Chase <cchase@redhat.com> - 0.0.1-1
- initial package
