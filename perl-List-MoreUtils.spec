%define modname List-MoreUtils
%define modver 0.430
# Fix circular build dependency:
# gprintify requires perl-List-MoreUtils
%define dont_gprintify 1

Summary:	Provide the stuff missing in List::Util 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/List::MoreUtils
Source0:	http://www.cpan.org/modules/by-module/List/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel >= 2:5.14.2-1
BuildRequires:	perl(Exporter::Tiny)
BuildArch:	noarch

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

All of its functions are implementable in one line of Perl code. Using
the functions from this module however should give slightly better performance
as everything is implemented in C.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%make_install

%check
# Make test seems to work only with a
# previously installed version of perl-List-MoreUtils
#make test

%files
%doc Changes
%{perl_vendorlib}/List
%{_mandir}/man3/*
