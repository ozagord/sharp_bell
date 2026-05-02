const mozjpeg = require('imagemin-mozjpeg');
// const jpegtran = require('imagemin-jpegtran');
// const jpegoptim = require('imagemin-jpegoptim');

module.exports = function(grunt) {
  grunt.config.set('imagemin', {
    imagemin: {
          options: {
              optimizationLevel: 7,
              svgoPlugins: [{removeViewBox: false}],
              progressive: true,
              // use: [jpegoptim()]
              use: [mozjpeg()] // Example plugin usage
          },
            files: [{
                expand: true,
                cwd: 'source/assets',
                //src: ['**/*.{png,jpg,gif}'],
                src: ['**/*.{png,jpg,gif}'],
                dest: './'
            }]
        }
  });
  grunt.loadNpmTasks('grunt-contrib-imagemin');
//  grunt.registerTask('default', ['imagemin']);

};
