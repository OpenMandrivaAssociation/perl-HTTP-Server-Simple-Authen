%define upstream_name    HTTP-Server-Simple-Authen
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Authentication plugin for HTTP::Server::Simple
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Authen::Simple)
BuildRequires: perl(HTTP::Server::Simple)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
HTTP::Server::Simple::Authen is an HTTP::Server::Simple plugin to allow
HTTP authentication. Authentication scheme is pluggable and you can use
whatever Authentication protocol that Authen::Simple supports.

You can use 'authenticate' method whatever you want to authenticate the
request. The method returns '$username' taken from the request if the
authentication is successful, and 'undef' otherwise. The code in the
/SYNOPSIS manpage requires authentication for all the requests and behaves
just the same as Apache's 'Require valid-user'.

The following code will explain more about conditioning.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


