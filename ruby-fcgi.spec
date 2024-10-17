%define upstream_name fcgi
%define name ruby-%{upstream_name}
%define version 0.8.8
%define release %mkrel 2

Summary:	FastCGI support library for Ruby
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		https://rubyforge.org/projects/fcgi/
Source0:	http://rubyforge.org/frs/download.php/69127/%{upstream_name}-%{version}.tgz
License:	GPL
Group:		Development/Ruby
Requires:	ruby 
BuildRequires: ruby-devel libfcgi-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
FastCGI is a language independent, scalable, open extension 
to CGI that provides high performance without the limitations 
of server specific APIs. 

This packages allows you to use ruby to write web applications using 
FastCGI.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
ruby setup.rb config
ruby setup.rb setup
 
%install
rm -rf %buildroot
ruby setup.rb install --prefix=%{buildroot}

%check
ruby setup.rb test

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc  README ChangeLog README.signals 
%{ruby_sitelibdir}/*
