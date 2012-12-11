%define upstream_name    HTTP-Server-Simple-Authen
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Authentication plugin for HTTP::Server::Simple
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Authen::Simple)
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 653596
- rebuild for updated spec-helper

* Wed Aug 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 565894
- import perl-HTTP-Server-Simple-Authen


* Wed Aug 04 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
