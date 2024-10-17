Name:		texlive-duotenzor
Version:	18728
Release:	2
Summary:	Drawing package for circuit and duotensor diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/duotenzor
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duotenzor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duotenzor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a drawing package for circuit and duotensor diagrams
within LaTeX documents. It consists of about eighty commands,
calling on TikZ for support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/duotenzor/duotenzor.sty
%doc %{_texmfdistdir}/doc/latex/duotenzor/README
%doc %{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.pdf
%doc %{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
