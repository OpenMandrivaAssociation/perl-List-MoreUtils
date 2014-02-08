%define upstream_name	 List-MoreUtils
%define upstream_version 0.33
# Fix circular build dependency:
# gprintify requires perl-List-MoreUtils
%define dont_gprintify 1

Summary:	Provide the stuff missing in List::Util 
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/List/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl-devel >= 2:5.14.2-1

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

All of its functions are implementable in one line of Perl code. Using
the functions from this module however should give slightly better performance
as everything is implemented in C.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%check
%make test

%files 
%doc Changes README
%{perl_vendorarch}/List
%{perl_vendorarch}/auto/List
%{_mandir}/*/*

