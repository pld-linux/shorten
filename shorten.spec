Summary:	Shorten - fast compression for waveform files
Summary(pl.UTF-8):	Shorten - szybka kompresja plików ze spróbkowanym dźwiękiem
Name:		shorten
Version:	3.6.1
Release:	1
License:	non-commercial distribution and encoding
Group:		Applications/Sound
Source0:	http://shnutils.freeshell.org/shorten/dist/src/%{name}-%{version}.tar.gz
# Source0-md5:	fb59c16fcedc4f4865d277f6e45866a7
URL:		http://shnutils.freeshell.org/shorten/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shorten provides compression for waveform files, such as RIFF WAVE
(.wav). Both lossless and lossy compression is supported at about 2:1
compression in the lossless case and up to 5:1 compression in the
lossy case.

%description -l pl.UTF-8
Shorten kompresuje pliki ze spróbkowanym dźwiękiem, takie jak RIFF
WAVE (.wav). Obsługiwana jest zarówno bezstratna jak i stratna
kompresja ze współczynnikiem około 2:1 w przypadku kompresji
bezstratnej i 5:1 w przypadku stratnej.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/LICENSE doc/tr156.ps
%attr(755,root,root) %{_bindir}/shorten
%{_mandir}/man1/shorten.1*
