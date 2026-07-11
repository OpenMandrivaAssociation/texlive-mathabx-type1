%global tl_name mathabx-type1
%global tl_revision 21129

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Outline version of the mathabx fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/mathabx
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mathabx)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an Adobe Type 1 outline version of the mathabx fonts.

