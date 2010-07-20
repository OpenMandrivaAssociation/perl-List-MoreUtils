%define upstream_name	 List-MoreUtils
%define upstream_version 0.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 3

Summary:	Provide the stuff missing in List::Util 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/List/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
Buildrequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
List::MoreUtils provides some trivial but commonly needed functionality on
lists which is not going to go into List::Util.

All of its functions are implementable in one line of Perl code. Using
the functions from this module however should give slightly better performance
as everything is implemented in C.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}_02

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/List
%{perl_vendorarch}/auto/List
%{_mandir}/*/*
