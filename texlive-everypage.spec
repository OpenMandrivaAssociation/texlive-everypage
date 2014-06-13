# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/everypage
# catalog-date 2008-02-19 19:31:19 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-everypage
Version:	1.1
Release:	7
Summary:	Provide hooks to be run on every page of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/everypage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everypage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides hooks to perform actions on every page, or
on the current page. Specifically, actions are performed after
the page is composed, but before it is shipped, so they can be
used to prepare the output page in tasks like putting
watermarks in the background, or in setting the next page
layout, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/everypage/everypage.sty
%doc %{_texmfdistdir}/doc/latex/everypage/README
%doc %{_texmfdistdir}/doc/latex/everypage/everypage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/everypage/everypage.dtx
%doc %{_texmfdistdir}/source/latex/everypage/everypage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 751670
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718393
- texlive-everypage
- texlive-everypage
- texlive-everypage
- texlive-everypage

