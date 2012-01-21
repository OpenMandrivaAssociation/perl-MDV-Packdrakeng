%define dist	MDV-Packdrakeng
%define version	1.13
%define release	%mkrel 9

# perl-Compress-Zlib is only "suggested"
%define _requires_exceptions perl(Compress::Zlib)

Name:		perl-%{dist}
Version:	%{version}
Release:	%{release}
Summary:	Simple Archive Extractor/Builder
License:	GPL
Group:		Development/Perl
Source0:	%{dist}-%{version}.tar.gz
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/MDV-Packdrakeng/
BuildRequires:	perl(Compress::Zlib)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor using
standard compression methods.

%prep
%setup -q -n %{dist}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/*/*
%{perl_vendorlib}/MDV/Packdrakeng
%{perl_vendorlib}/MDV/Packdrakeng.pm

