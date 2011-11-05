# revision 21129
# category Package
# catalog-ctan /fonts/ps-type1/mathabx
# catalog-date 2011-01-19 07:58:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-mathabx-type1
Version:	20110119
Release:	1
Summary:	Outline version of the mathabx fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ps-type1/mathabx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx-type1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathabx-type1.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-mathabx
Conflicts:	texlive-texmf <= 20110705-3

%description
This is an Adobe Type 1 outline version of the mathabx fonts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/mathabx-type1/mathabx.map
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha12.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha5.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha6.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha7.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha8.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha9.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathastrotest10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb12.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb5.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb6.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb7.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb8.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb9.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathc10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathu10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathux10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx10.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx12.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx5.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx6.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx7.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx8.pfb
%{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx9.pfb
%doc %{_texmfdistdir}/doc/fonts/mathabx-type1/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
