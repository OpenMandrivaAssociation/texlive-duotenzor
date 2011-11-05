# revision 18728
# category Package
# catalog-ctan /graphics/duotenzor
# catalog-date 2010-06-06 13:50:32 +0200
# catalog-license lppl1.3
# catalog-version 1.00
Name:		texlive-duotenzor
Version:	1.00
Release:	1
Summary:	Drawing package for circuit and duotensor diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/duotenzor
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duotenzor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duotenzor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a drawing package for circuit and duotensor diagrams
within LaTeX documents. It consists of about eighty commands,
calling on TikZ for support.

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
%{_texmfdistdir}/tex/latex/duotenzor/duotenzor.sty
%doc %{_texmfdistdir}/doc/latex/duotenzor/README
%doc %{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.pdf
%doc %{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
