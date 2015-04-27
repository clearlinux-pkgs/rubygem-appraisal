Name     : rubygem-appraisal
Version  : 2.0.2
Release  : 7
URL      : https://rubygems.org/downloads/appraisal-2.0.2.gem
Source0  : https://rubygems.org/downloads/appraisal-2.0.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-appraisal-bin
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-appraisal
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-i18n
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-thor
BuildRequires : rubygem-thread_safe
BuildRequires : rubygem-tzinfo
Patch1: 0001-Fix-thor-version.patch

%description
Appraisal
=========
[![Build Status][Build Status Image]][Build Status]
Find out what your Ruby gems are worth.

%package bin
Summary: bin components for the rubygem-appraisal package.
Group: Binaries

%description bin
bin components for the rubygem-appraisal package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n appraisal-2.0.2
gem spec %{SOURCE0} -l --ruby > rubygem-appraisal.gemspec
%patch1 -p1

%build
gem build rubygem-appraisal.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
appraisal-2.0.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/appraisal-2.0.2
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/appraisal-2.0.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/bundle_parallel_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/cdesc-Appraisal.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/check_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/clean_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gemfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gemfile_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gemfile_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gemfile_root-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/git-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/install-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/install_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/lockfile_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/platforms-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/relative_gemfile_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/relativize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/ruby-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/update-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/update_command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Appraisal/write_gemfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/AppraisalsNotFound/cdesc-AppraisalsNotFound.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/AppraisalsNotFound/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/cdesc-BundlerDSL.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/dependencies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/for_dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/git-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/indent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/platform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/platforms-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/ruby-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/ruby_version_entry-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/ruby_version_entry_for_dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/source_entry-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/source_entry_for_dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/BundlerDSL/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/cdesc-CLI.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/clean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/exit_on_failure%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/generate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/install-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/strip_heredoc-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/update-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/CLI/version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/announce-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/cdesc-Command.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/command-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/command_as_string-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/command_starting_with_bundle-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/command_starts_with_bundle%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/ensure_bundler_is_available-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/gemfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/original_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/restore_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/unset_bundler_env_vars-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Command/with_clean_env-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Dependency/cdesc-Dependency.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Dependency/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Dependency/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Dependency/requirements-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Dependency/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/DependencyList/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/DependencyList/cdesc-DependencyList.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/DependencyList/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/DependencyList/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/appraisals-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/appraise-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/cdesc-File.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/each-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/gemfile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/File/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemfile/cdesc-Gemfile.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemfile/dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemfile/load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemfile/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemspec/cdesc-Gemspec.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemspec/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemspec/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Gemspec/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/GitSource/cdesc-GitSource.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/GitSource/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/GitSource/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Group/cdesc-Group.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Group/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Group/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/OrderedHash/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/OrderedHash/cdesc-OrderedHash.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/OrderedHash/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/OrderedHash/values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/PathSource/cdesc-PathSource.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/PathSource/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/PathSource/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Platform/cdesc-Platform.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Platform/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Platform/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Task/cdesc-Task.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Task/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/cdesc-ConfigurationValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/configuration-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/has_configuration_file%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/has_invalid_gemfiles_configuration%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/has_no_gemfiles_configuration%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/ConfigurationValidator/validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/cdesc-TravisCIHelper.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/display_instruction-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/TravisCIHelper/validate_configuration_file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/cdesc-Utils.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/format_arguments-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/format_string-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/join_parts-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/prefix_path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/Utils/support_parallel_installation%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/Appraisal/cdesc-Appraisal.ri
/usr/lib64/ruby/gems/2.2.0/doc/appraisal-2.0.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/.travis.yml
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/Gemfile.lock
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/appraisal.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/bin/appraisal
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/appraisal.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/bundler_dsl.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/cli.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/command.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/dependency.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/dependency_list.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/errors.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/file.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/gemfile.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/gemspec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/git_source.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/group.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/ordered_hash.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/path_source.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/platform.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/task.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/travis_ci_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/utils.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/lib/appraisal/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/appraisals_file_bundler_dsl_compatibility_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/bundle_with_custom_path_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/clean_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/generate_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/help_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/install_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/list_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/run_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/update_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/version_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/cli/with_no_arguments_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/gemfile_dsl_compatibility_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/gemspec_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/acceptance/travis_ci_integration_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/appraisal/appraisal_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/appraisal/dependency_list_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/appraisal/file_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/appraisal/gemfile_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/appraisal/utils_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/support/acceptance_test_helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/support/dependency_helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/spec/support/stream_helpers.rb
%exclude /usr/lib64/ruby/gems/2.2.0/gems/appraisal-2.0.2/tmp/*
/usr/lib64/ruby/gems/2.2.0/specifications/appraisal-2.0.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/appraisal
