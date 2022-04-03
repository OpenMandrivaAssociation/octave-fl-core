%define octpkg fl-core

Summary:	The package contains code for basic functions in Fuzzy Logic for Octave
Name:		octave-%{octpkg}
Version:	1.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.0.tar.gz
# https://savannah.gnu.org/bugs/?func=detailitem&item_id=48334
Patch0:		%{name}-1.0.0-fix-include.patch
License:	LGPL v3
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 2.9.7

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The package contains code for basic functions in Fuzzy Logic for Octave.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild
