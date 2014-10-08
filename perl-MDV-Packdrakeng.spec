%define dist MDV-Packdrakeng

# perl-Compress-Zlib is only "suggested"
%define __noautoreq 'perl\\(Compress::Zlib\\)'

Summary:	Simple Archive Extractor/Builder
Name:		perl-%{dist}
Version:	1.14
Release:	9
License:	GPLv2+
Group:		Development/Perl
Url:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/MDV-Packdrakeng/
Source0:	%{dist}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel
Suggests:	perl(Compress::Zlib)

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor using
standard compression methods.

%prep
%setup -qn %{dist}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/MDV/Packdrakeng
%{perl_vendorlib}/MDV/Packdrakeng.pm
%{_mandir}/man3/*

