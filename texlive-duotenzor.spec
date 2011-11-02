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
Requires(post):	texlive-tlpkg
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
