%define rname fcgi
%define name ruby-%{rname}
%define version 0.8.7
%define release %mkrel 3

Summary:	FastCGI support library for Ruby
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://rubyforge.org/projects/fcgi/
Source0:	http://www.moonwolf.com/ruby/archive/%{name}-%{version}.tar.gz
License:	GPL
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	ruby 
BuildRequires: ruby-devel libfcgi-devel
%description
FastCGI is a language independent, scalable, open extension 
to CGI that provides high performance without the limitations 
of server specific APIs. 

This packages allows you to use ruby to write web applications using 
FastCGI.
%prep
%setup -q 

%build
ruby install.rb config 
ruby install.rb setup
 
%install
rm -rf %buildroot
ruby install.rb install --prefix=$RPM_BUILD_ROOT 

%check
ruby install.rb test

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc  README ChangeLog README.signals 
%{ruby_sitelibdir}/*
