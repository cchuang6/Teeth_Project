Menubar.File = function ( editor ) {

	var container = new UI.Panel();
	container.setClass( 'menu' );
	container.onMouseOver( function () { options.setDisplay( 'block' ) } );
	container.onMouseOut( function () { options.setDisplay( 'none' ) } );
	container.onClick( function () { options.setDisplay( 'block' ) } );

	var title = new UI.Panel();
	title.setTextContent( 'File' );
	title.setMargin( '0px' );
	title.setPadding( '8px' );
	container.add( title );

	//

	var options = new UI.Panel();
	options.setClass( 'options' );
	options.setDisplay( 'none' );
	container.add( options );

	// new

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'New' );
	option.onClick( function () {

		if ( confirm( 'Are you sure?' ) ) {

			editor.config.clear();
			editor.storage.clear( function () {
				
				location.href = location.pathname;

			} );

		}

	} );
	console.log('New in option');
	options.add( option );

	options.add( new UI.HorizontalRule() );


	// import

	var input = document.createElement( 'input' );
	input.type = 'file';
	input.addEventListener( 'change', function ( event ) {
		console.log("add file");
		console.log(input.files[0]);		
		editor.loader.loadFile( input.files[ 0 ] );
		
	} );

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Import' );
	option.onClick( function () {

		input.click();

	} );
	options.add( option );

	options.add( new UI.HorizontalRule() );


	// export geometry

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Export Geometry' );
	option.onClick( function () {

		var geometry = editor.selected.geometry;

		if ( geometry instanceof THREE.BufferGeometry ) {

			exportGeometry( THREE.BufferGeometryExporter );

		} else if ( geometry instanceof THREE.Geometry ) {

			exportGeometry( THREE.GeometryExporter );

		}

	} );
	options.add( option );

	/*

	// export scene

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Export Scene' );
	option.onClick( function () {

		exportScene( THREE.SceneExporter );

	} );
	options.add( option );

	*/

	// export object

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Export Object' );
	option.onClick( function () {

		exportObject( THREE.ObjectExporter );

	} );
	options.add( option );

	// export scene

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Export Scene' );
	option.onClick( function () {

		exportScene( THREE.ObjectExporter );

	} );
	options.add( option );

	// export OBJ

	var option = new UI.Panel();
	option.setClass( 'option' );
	option.setTextContent( 'Export OBJ' );
	option.onClick( function () {

		exportGeometry( THREE.OBJExporter );

	} );
	options.add( option );

	var exportGeometry = function ( exporterClass ) {

		var object = editor.selected;

		if ( object.geometry === undefined ) {

			alert( "Selected object doesn't have any geometry" );
			return;

		}

		var exporter = new exporterClass();

		var output;

		if ( exporter instanceof THREE.BufferGeometryExporter || exporter instanceof THREE.GeometryExporter ) {

			output = JSON.stringify( exporter.parse( object.geometry ), null, '\t' );
			output = output.replace( /[\n\t]+([\d\.e\-\[\]]+)/g, '$1' );

		} else {

			output = exporter.parse( object.geometry );

		}

		var blob = new Blob( [ output ], { type: 'text/plain' } );
		var objectURL = URL.createObjectURL( blob );

		window.open( objectURL, '_blank' );
		window.focus();

	};

	var exportObject = function ( exporterClass ) {

		var exporter = new exporterClass();

		var object = editor.selected;

		var output = JSON.stringify( exporter.parse( object ), null, '\t' );
		output = output.replace( /[\n\t]+([\d\.e\-\[\]]+)/g, '$1' );

		var blob = new Blob( [ output ], { type: 'text/plain' } );
		var objectURL = URL.createObjectURL( blob );
		downloadURL(objectURL);
		window.open( objectURL, '_blank' );
		window.focus();

	};

	var exportScene = function ( exporterClass ) {

		var exporter = new exporterClass();

		var output = JSON.stringify( exporter.parse( editor.scene ), null, '\t' );
		output = output.replace( /[\n\t]+([\d\.e\-\[\]]+)/g, '$1' );

		var blob = new Blob( [ output ], { type: 'text/plain' } );
		var objectURL = URL.createObjectURL( blob );

		window.open( objectURL, '_blank' );
		window.focus();

	};
	
	var downloadURL = function downloadURL(url) {
		var hiddenIFrameID = 'hiddenDownloader', iframe = document.getElementById(hiddenIFrameID);
		if (iframe === null) {
			iframe = document.createElement('iframe');
			iframe.id = hiddenIFrameID;
			iframe.style.display = 'none';
			document.body.appendChild(iframe);
		}
		iframe.src = url;
	};

	return container;

}
